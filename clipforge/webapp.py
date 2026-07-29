"""
Local web UI for clipforge.

Submit a title, watch the pipeline (script -> TTS -> subtitles -> clips ->
compose) run live, and see the total generation time. Single-job-at-a-time
(this is a local single-user tool, not a queueing service).
"""

import json
import logging
import queue
import shutil
import threading
import time
import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from pydantic import BaseModel

from .config import get_config
from .pipeline import run_pipeline, tmp_dir_for
from .story import STYLES, generate_story, generate_title_suggestions
from .visuals import GenerationCancelled

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

app = FastAPI(title="ClipForge")

_WEB_DIR = Path(__file__).parent / "web"
_lock = threading.Lock()


class Job:
    def __init__(self, job_id: str, clips_dir: Path):
        self.id = job_id
        self.clips_dir = clips_dir
        self.events: "queue.Queue[dict]" = queue.Queue()
        self.status = "running"
        self.output_path: Optional[Path] = None
        self.error: Optional[str] = None
        self.start_time = time.monotonic()
        self.cancel_event = threading.Event()

    def run(self, **kwargs) -> None:
        try:
            self.output_path = run_pipeline(
                progress_sink=self.events.put, keep_intermediates=True,
                cancel_event=self.cancel_event, **kwargs,
            )
            self.status = "done"
        except GenerationCancelled:
            self.status = "cancelled"
        except Exception as exc:
            self.status = "error"
            self.error = str(exc)
        finally:
            elapsed = round(time.monotonic() - self.start_time, 2)
            level = {"done": "DONE", "cancelled": "CANCELLED"}.get(self.status, "ERROR")
            message = {"done": "Done", "cancelled": "Cancelled"}.get(self.status, self.error)
            self.events.put({
                "t": elapsed,
                "logger": "clipforge.webapp",
                "level": level,
                "message": message,
                "final": True,
                "status": self.status,
                "elapsed": elapsed,
                "video_url": f"/api/video/{self.id}" if self.status == "done" else None,
            })


_current_job: Optional[Job] = None


class TitleSuggestRequest(BaseModel):
    style: str = "mind_blowing"


class ScriptRequest(BaseModel):
    title: str
    style: str = "mind_blowing"
    length_seconds: float = 60.0


class GenerateRequest(BaseModel):
    title: str
    style: str = "mind_blowing"
    length_seconds: float = 60.0
    voice: Optional[str] = None
    script: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return (_WEB_DIR / "index.html").read_text()


@app.get("/api/styles")
def list_styles() -> dict:
    return STYLES


@app.post("/api/suggest-titles")
def suggest_titles(req: TitleSuggestRequest) -> dict:
    """Suggest 3 viral title/topic ideas for the chosen style."""
    config = get_config()
    try:
        titles = generate_title_suggestions(style=req.style, config=config)
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(400, str(exc))
    return {"titles": titles}


@app.post("/api/generate-script")
def generate_script(req: ScriptRequest) -> dict:
    """Generate just the narration script, for the user to review before
    committing to the (costly) TTS + visuals + compose stages."""
    config = get_config()
    try:
        script = generate_story(
            style=req.style, topic=req.title,
            target_seconds=req.length_seconds, config=config,
        )
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(400, str(exc))
    return {"script": script}


@app.post("/api/generate")
def generate(req: GenerateRequest) -> dict:
    global _current_job
    with _lock:
        if _current_job is not None and _current_job.status == "running":
            raise HTTPException(409, "A generation job is already running")

        # Previous job's intermediates (kept around for hover previews) are
        # no longer needed once a new job starts.
        if _current_job is not None:
            shutil.rmtree(_current_job.clips_dir.parent, ignore_errors=True)

        job_id = uuid.uuid4().hex[:8]
        config = get_config()
        config.ensure_output_dir()
        output_path = config.output_dir / f"clipforge_{job_id}.mp4"
        clips_dir = tmp_dir_for(output_path) / "clips"

        job = Job(job_id, clips_dir)
        _current_job = job

        thread = threading.Thread(
            target=job.run,
            kwargs=dict(
                topic=req.title,
                script=req.script,
                style=req.style,
                voice=req.voice,
                length_seconds=req.length_seconds,
                output=output_path,
                config=config,
            ),
            daemon=True,
        )
        thread.start()

    return {"job_id": job_id}


@app.post("/api/cancel/{job_id}")
def cancel(job_id: str) -> dict:
    job = _current_job
    if job is None or job.id != job_id:
        raise HTTPException(404, "Unknown job")
    if job.status != "running":
        raise HTTPException(409, f"Job is already {job.status}")
    job.cancel_event.set()
    return {"status": "cancelling"}


@app.get("/api/events/{job_id}")
def events(job_id: str) -> StreamingResponse:
    job = _current_job
    if job is None or job.id != job_id:
        raise HTTPException(404, "Unknown job")

    def stream():
        while True:
            event = job.events.get()
            yield f"data: {json.dumps(event)}\n\n"
            if event.get("final"):
                break

    return StreamingResponse(stream(), media_type="text/event-stream")


@app.get("/api/video/{job_id}")
def get_video(job_id: str) -> FileResponse:
    job = _current_job
    if job is None or job.id != job_id or job.status != "done" or not job.output_path:
        raise HTTPException(404, "Video not ready")
    return FileResponse(job.output_path, media_type="video/mp4")


@app.get("/api/preview/{job_id}/{filename}")
def get_preview(job_id: str, filename: str) -> FileResponse:
    """Serve a single scene's generated image or clip for hover previews."""
    job = _current_job
    if job is None or job.id != job_id:
        raise HTTPException(404, "Unknown job")

    # Strip any path components — filename must resolve to a direct child
    # of this job's clips directory, nothing else on disk.
    safe_name = Path(filename).name
    path = job.clips_dir / safe_name
    if path.parent != job.clips_dir or not path.is_file():
        raise HTTPException(404, "Preview not found")

    media_type = "image/png" if path.suffix == ".png" else "video/mp4"
    return FileResponse(path, media_type=media_type)
