"""
Reusable end-to-end generation pipeline with live progress capture.

Runs the same steps as ``clipforge generate`` (script -> TTS -> subtitles ->
visual clips -> compose), but can forward every clipforge log record to a
caller-supplied sink as a structured event — used by the web UI to stream
live progress instead of just printing to stdout.
"""

import logging
import shutil
import threading
import time
from pathlib import Path
from typing import Callable, Optional

from .config import Config, get_config
from .visuals import GenerationCancelled

ProgressSink = Callable[[dict], None]


def _check_cancel(cancel_event: Optional[threading.Event]) -> None:
    if cancel_event is not None and cancel_event.is_set():
        raise GenerationCancelled("Cancelled")


def tmp_dir_for(output_path: Path) -> Path:
    """The scratch directory a run_pipeline() call uses for a given output path.

    Exposed so callers that keep intermediates around (e.g. the web UI, for
    clip/image hover previews) can find them without duplicating the naming
    convention.
    """
    output_path = Path(output_path)
    return output_path.parent / f".clipforge_tmp_{output_path.stem}"


class _ProgressCaptureHandler(logging.Handler):
    """Forwards clipforge log records to a sink as structured progress events."""

    def __init__(self, sink: ProgressSink, start_time: float):
        super().__init__(level=logging.INFO)
        self._sink = sink
        self._start_time = start_time

    def emit(self, record: logging.LogRecord) -> None:
        # visuals.py tags records with which concurrent scene worker emitted
        # them (scenes now generate in parallel) — pass it through so a
        # listener can route per-scene status without assuming log order.
        scene_idx = getattr(record, "scene_idx", None)
        self._sink({
            "t": round(time.monotonic() - self._start_time, 2),
            "logger": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
            "scene_idx": scene_idx,
        })


def run_pipeline(
    topic: Optional[str] = None,
    script: Optional[str] = None,
    style: str = "mind_blowing",
    voice: Optional[str] = None,
    length_seconds: float = 60.0,
    output: Optional[Path] = None,
    music: Optional[Path] = None,
    config: Optional[Config] = None,
    progress_sink: Optional[ProgressSink] = None,
    keep_intermediates: bool = False,
    cancel_event: Optional[threading.Event] = None,
) -> Path:
    """Run the full generate pipeline, optionally streaming progress events.

    Args:
        topic: Topic for AI story generation (ignored if ``script`` is set).
        script: Custom script text (skips AI story generation).
        style: Content style key for AI story generation.
        voice: TTS voice name or shorthand.
        length_seconds: Desired video length in seconds (ignored if
            ``script`` is set — a custom script's own length just plays out).
            Drives both the generated script's word count and, from the
            actual narrated audio, how many visual scenes are cut.
        output: Output video path (defaults to ``{output_dir}/short.mp4``).
        music: Optional background music file.
        config: Configuration instance.
        progress_sink: Optional callback invoked with a structured event dict
            for every clipforge log line emitted during the run.
        keep_intermediates: If True, don't delete the per-scene images/clips
            scratch directory (see ``tmp_dir_for``) after composing — used
            by the web UI to serve clip/image hover previews.
        cancel_event: If set, stops the run at the next checked point (stage
            boundaries, and between scenes during clip generation) rather
            than immediately — an in-flight API call still finishes first.

    Returns:
        Path to the composed output video.

    Raises:
        RuntimeError: If neither a topic/LLM key nor a script is available.
        GenerationCancelled: If ``cancel_event`` is set during the run.
    """
    config = config or get_config()
    log = logging.getLogger("clipforge.pipeline")
    root_logger = logging.getLogger("clipforge")

    start_time = time.monotonic()
    handler: Optional[_ProgressCaptureHandler] = None
    if progress_sink:
        handler = _ProgressCaptureHandler(progress_sink, start_time)
        root_logger.addHandler(handler)

    try:
        if output:
            output_path = Path(output)
        else:
            config.ensure_output_dir()
            output_path = config.output_dir / "short.mp4"

        if script:
            story = script
            log.info("Using custom script (%d words)", len(story.split()))
            log.info("Script: %s", story)
        elif topic or config.has_llm:
            if not config.has_llm:
                raise RuntimeError(
                    "No LLM API key set. Set CLIPFORGE_LLM_KEY or provide a script."
                )
            from .story import generate_story
            log.info("Generating %s story (topic: %s)...", style, topic or "random")
            story = generate_story(
                style=style, topic=topic, target_seconds=length_seconds, config=config,
            )
            log.info("Story generated (%d words)", len(story.split()))
            log.info("Script: %s", story)
        else:
            raise RuntimeError("Provide a topic, script, or set CLIPFORGE_LLM_KEY.")

        _check_cancel(cancel_event)

        from .voice import generate_speech
        tmp_dir = tmp_dir_for(output_path)
        tmp_dir.mkdir(parents=True, exist_ok=True)
        audio_path = tmp_dir / "voice.mp3"

        log.info("Generating TTS narration...")
        word_data = generate_speech(story, audio_path, voice=voice, config=config)

        _check_cancel(cancel_event)

        from .subtitles import generate_subtitles
        subs_path = tmp_dir / "subs.ass"
        log.info("Generating subtitles...")
        generate_subtitles(word_data, subs_path)

        _check_cancel(cancel_event)

        from .visuals import generate_clips
        clips_dir = tmp_dir / "clips"
        log.info("Generating visual clips...")
        clips = generate_clips(
            story, clips_dir, word_data=word_data, config=config,
            keep_images=keep_intermediates, cancel_event=cancel_event,
        )
        log.info("Generated %d clips", len(clips))

        _check_cancel(cancel_event)

        from .compose import compose_video
        log.info("Composing final video...")
        music_path = Path(music) if music else None
        compose_video(
            clips=clips, audio=audio_path, subs=subs_path,
            output=output_path, music=music_path,
        )

        elapsed = time.monotonic() - start_time
        log.info("Done! Video saved to: %s (%.1fs total)", output_path, elapsed)

        if not keep_intermediates:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        return output_path
    finally:
        if handler:
            root_logger.removeHandler(handler)
