"""
AI visual generation for clipforge.

Generates contextual images via Replicate's Flux Schnell and animates them
into motion clips via Replicate's image-to-video model (prunaai/p-video).
Image generation retries on failure and rewords the prompt via LLM after
repeated failures — no gradient fallback for image-generation errors.
Falls back to a Ken Burns zoom/pan clip if i2v generation fails, and to a
solid gradient clip only when no scene prompt is available at all (AI
disabled or scene extraction failed).
"""

import concurrent.futures
import json
import logging
import random
import re
import subprocess
import threading
import uuid
from pathlib import Path
from typing import Optional

from .config import Config, get_config
from .story import _call_llm

log = logging.getLogger("clipforge.visuals")


class GenerationCancelled(Exception):
    """Raised when a running pipeline is asked to stop mid-generation."""


# Scenes generate concurrently, one worker thread per in-flight scene, up to
# this many at once — bounded because Replicate throttles low-credit accounts
# to a handful of requests per minute, so uncapped concurrency just trades
# wall-clock time for a wall of 429 retries instead of a real speedup.
MAX_CONCURRENT_SCENES = 3

# Attaches the current worker thread's scene index to every log record it
# emits, since scenes now run concurrently and their log lines interleave —
# the web UI needs this to route "generating image…" etc. to the right card.
_scene_context = threading.local()


class _SceneIndexFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.scene_idx = getattr(_scene_context, "index", None)
        return True


log.addFilter(_SceneIndexFilter())

# Target average seconds per visual scene — used to derive how many scenes
# to aim for from the actual narrated audio duration.
TARGET_SCENE_SECONDS = 4.5

# Used only when TTS produced no word timestamps at all (last-resort pacing).
WORDS_PER_SECOND_FALLBACK = 2.5

# ── Cinematic prompt suffixes ────────────────────────────────────────────────

CINEMATIC_SUFFIXES: list[str] = [
    "cinematic lighting, dramatic atmosphere, 4K, photorealistic, film grain",
    "cinematic, moody lighting, ultra detailed, photorealistic, shallow depth of field",
    "dramatic lighting, volumetric fog, photorealistic, cinematic composition, 4K",
    "epic cinematic shot, hyper-realistic, dramatic shadows, professional photography",
    "cinematic wide shot, dramatic golden hour lighting, photorealistic, ultra sharp",
    "dark cinematic tone, high contrast, photorealistic, dramatic chiaroscuro",
    "neon-lit cinematic, cyberpunk atmosphere, ultra detailed, photorealistic",
    "atmospheric fog, cinematic color grading, photorealistic, wide angle lens",
]

# ── Gradient color palettes for fallback clips ───────────────────────────────

GRADIENT_PALETTES: list[tuple[str, str]] = [
    ("0x0b0b2e", "0x1a0a3a"),  # deep indigo
    ("0x1a0000", "0x0a0a2e"),  # dark red to navy
    ("0x001a1a", "0x0a0a2e"),  # teal to navy
    ("0x1a1a00", "0x0a002e"),  # olive to purple
    ("0x0d1117", "0x161b22"),  # github dark
    ("0x0f0c29", "0x302b63"),  # midnight purple
    ("0x000428", "0x004e92"),  # deep ocean
    ("0x1f1c2c", "0x928dab"),  # dusty lavender
]


def _enhance_prompt(scene: str) -> str:
    """Turn a scene description into a cinematic AI image prompt."""
    suffix = random.choice(CINEMATIC_SUFFIXES)
    return (
        f"{scene}, {suffix}. "
        f"No text, no words, no letters, no watermark, no UI elements. "
        f"Portrait orientation 9:16, vertical composition."
    )


# ── Scene segmentation (timing-aware) ────────────────────────────────────────

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_CLAUSE_SPLIT_RE = re.compile(r"(?<=[.!?,;])\s+")


_MAX_SENTENCE_WORDS = 30


def _split_sentences(story: str) -> list[str]:
    """Split a story into sentences (simple punctuation-based split).

    Falls back to splitting on clause boundaries (commas/semicolons) if the
    whole story comes back as one long comma-spliced run-on with no other
    terminal punctuation — otherwise there'd be nothing to segment into
    more than one scene. Also re-splits any *individual* sentence that's
    unusually long the same way: an LLM ignoring length guidance for just
    one sentence would otherwise become one scene that can't be subdivided
    further downstream (split_long_segments only splits across multiple
    sentences, not within one).
    """
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(story.strip()) if s.strip()]
    if len(sentences) <= 1 and len(story.split()) > 20:
        sentences = [s.strip() for s in _CLAUSE_SPLIT_RE.split(story.strip()) if s.strip()]

    refined: list[str] = []
    for sentence in sentences:
        if len(sentence.split()) > _MAX_SENTENCE_WORDS:
            refined.extend(
                s.strip() for s in _CLAUSE_SPLIT_RE.split(sentence) if s.strip()
            )
        else:
            refined.append(sentence)

    return refined or [story.strip()]


def _fallback_segments(sentences: list[str], target_scene_count: int) -> list[dict]:
    """Deterministically group sentences into scenes by word count (no LLM)."""
    total_words = sum(len(s.split()) for s in sentences) or 1
    words_per_scene = max(1, round(total_words / target_scene_count))

    segments: list[dict] = []
    current_indices: list[int] = []
    current_words = 0

    for i, sentence in enumerate(sentences):
        current_indices.append(i)
        current_words += len(sentence.split())
        is_last = i == len(sentences) - 1
        if current_words >= words_per_scene and not is_last:
            text = " ".join(sentences[j] for j in current_indices)
            segments.append({
                "sentence_indices": current_indices,
                "text": text,
                "prompt": f"cinematic scene depicting: {text[:80]}",
            })
            current_indices = []
            current_words = 0

    if current_indices:
        text = " ".join(sentences[j] for j in current_indices)
        segments.append({
            "sentence_indices": current_indices,
            "text": text,
            "prompt": f"cinematic scene depicting: {text[:80]}",
        })

    return segments


def segment_story_into_scenes(
    story: str,
    target_scene_count: int,
    config: Optional[Config] = None,
) -> list[dict]:
    """Split a story into scenes aligned to its actual sentences.

    Asks the LLM to group sentence INDICES (not free-invented text) into
    roughly ``target_scene_count`` visual scenes with an image prompt each.
    Grouping by index (rather than asking the LLM to reproduce text
    verbatim) keeps the mapping back to the original sentences exact, which
    is what lets clip durations later be aligned to real narration
    timestamps instead of being guessed.

    Args:
        story: The narrated story text.
        target_scene_count: Rough number of scenes to aim for.
        config: Configuration instance.

    Returns:
        Ordered list of ``{"sentence_indices": [...], "text": ..., "prompt": ...}``.
    """
    config = config or get_config()
    sentences = _split_sentences(story)
    target_scene_count = max(1, min(target_scene_count, len(sentences)))

    if not config.has_llm:
        return _fallback_segments(sentences, target_scene_count)

    numbered = "\n".join(f"[{i}] {s}" for i, s in enumerate(sentences))
    prompt = f"""Group these numbered sentences from a video script into roughly {target_scene_count} visual scenes for AI image generation.

Sentences:
{numbered}

Rules:
- Every sentence index (0 to {len(sentences) - 1}) must appear in exactly one scene, in order, with no gaps or overlaps
- Group sentences that share the same imagery/moment together; start a new scene when the visual should change
- Aim for about {target_scene_count} scenes total, but let natural scene changes decide — a few more or fewer is fine
- For each scene, write a vivid, specific image prompt (15-30 words) describing what we SEE — setting, lighting, mood, key visual elements
- NO text, NO people's faces in close-up (avoid uncanny valley)
- Make it cinematic and dramatic

Return ONLY a JSON array, nothing else:
[{{"sentences": [0, 1], "prompt": "scene description"}}, ...]"""

    try:
        text = _call_llm(prompt, config, max_tokens=1500, temperature=0.6)
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip()

        raw_scenes = json.loads(text)
        if not isinstance(raw_scenes, list) or not raw_scenes:
            raise ValueError("empty or non-list response")

        expected = set(range(len(sentences)))
        seen: list[int] = []
        segments: list[dict] = []
        for scene in raw_scenes:
            indices = sorted(int(i) for i in scene["sentences"])
            seen.extend(indices)
            text_span = " ".join(
                sentences[i] for i in indices if 0 <= i < len(sentences)
            )
            segments.append({
                "sentence_indices": indices,
                "text": text_span,
                "prompt": scene["prompt"],
            })

        if set(seen) != expected:
            raise ValueError(f"sentence coverage mismatch: got {sorted(set(seen))}")

        return segments
    except (json.JSONDecodeError, ValueError, KeyError, TypeError, RuntimeError) as exc:
        log.warning("Scene segmentation failed: %s — using word-count fallback", exc)
        return _fallback_segments(sentences, target_scene_count)


def compute_scene_timings(
    segments: list[dict],
    sentences: list[str],
    word_data: list[dict],
) -> list[dict]:
    """Attach start/end/duration (seconds) to each scene from TTS word timestamps.

    Aligns by proportional word position rather than assuming this module's
    ``str.split()`` word count exactly matches the TTS engine's own word
    boundaries (numbers, contractions, etc. can tokenize slightly
    differently) — this keeps timing correct even when counts drift a bit.

    Args:
        segments: Scenes from ``segment_story_into_scenes``.
        sentences: The same sentence list used to build ``segments``.
        word_data: TTS word-timestamp list from ``voice.generate_speech``.

    Returns:
        Segments with ``start``, ``end``, and ``duration`` (seconds) added.
    """
    if not word_data:
        segments_out = []
        t = 0.0
        for seg in segments:
            dur = max(2.0, len(seg["text"].split()) / WORDS_PER_SECOND_FALLBACK)
            segments_out.append({**seg, "start": t, "end": t + dur, "duration": dur})
            t += dur
        return segments_out

    sentence_word_counts = [len(s.split()) for s in sentences]
    cum_words = [0]
    for count in sentence_word_counts:
        cum_words.append(cum_words[-1] + count)
    total_words = cum_words[-1] or 1
    n_words_tts = len(word_data)

    def word_time(word_idx: int) -> float:
        scaled = max(0, min(round(word_idx * n_words_tts / total_words), n_words_tts - 1))
        return word_data[scaled]["start"]

    def word_end_time(word_idx: int) -> float:
        scaled = max(0, min(round(word_idx * n_words_tts / total_words) - 1, n_words_tts - 1))
        w = word_data[scaled]
        return w["start"] + w["duration"]

    audio_end = word_data[-1]["start"] + word_data[-1]["duration"]

    out = []
    for seg in segments:
        first_sentence = min(seg["sentence_indices"])
        last_sentence = max(seg["sentence_indices"])
        word_start = cum_words[first_sentence]
        word_end = cum_words[last_sentence + 1]

        start = word_time(word_start) if word_start > 0 else 0.0
        end = word_end_time(word_end) if word_end < total_words else audio_end
        end = max(end, start + 1.0)

        out.append({**seg, "start": start, "end": end, "duration": end - start})

    return out


def split_long_segments(segments: list[dict], max_duration: float) -> list[dict]:
    """Split any scene that grew too long into two back-to-back scenes.

    The LLM sometimes groups several sentences into one visual scene when
    it judges they share the same imagery — reasonable for pacing, but if
    that scene ends up spanning a large chunk of the video, one static
    image/motion clip would dominate the screen for too long. This splits
    the sentence range roughly in half (reusing the same image prompt —
    each generation is non-deterministic anyway, so the two halves won't
    look identical) rather than dropping content or re-calling the LLM.

    Args:
        segments: Timed scenes from ``compute_scene_timings``.
        max_duration: Longest a single scene is allowed to be, in seconds.

    Returns:
        Segments with any over-long scene split into two.
    """
    changed = True
    while changed:
        changed = False
        out: list[dict] = []
        for seg in segments:
            if seg["duration"] <= max_duration or len(seg["sentence_indices"]) < 2:
                out.append(seg)
                continue

            indices = seg["sentence_indices"]
            mid = len(indices) // 2
            first_indices, second_indices = indices[:mid], indices[mid:]
            split_time = seg["start"] + seg["duration"] * (len(first_indices) / len(indices))

            out.append({
                **seg,
                "sentence_indices": first_indices,
                "end": split_time,
                "duration": split_time - seg["start"],
            })
            out.append({
                **seg,
                "sentence_indices": second_indices,
                "start": split_time,
                "end": seg["end"],
                "duration": seg["end"] - split_time,
            })
            changed = True
        segments = out
    return segments


# ── Motion prompt generation ─────────────────────────────────────────────────

_MOTION_NEGATIVE_TAIL = (
    "No exaggerated acting, no sudden movements, no camera shake, no zoom jumps, "
    "no scene transition, no change in lighting, no change in clothing, no "
    "additional people, no object deformation, no morphing, no warped hands or "
    "fingers, no unnatural limb movement, no facial distortion, no text, no "
    "subtitles, no letters, no watermark, no UI elements. Photorealistic "
    "cinematic motion, emotionally restrained, realistic micro-expressions, "
    "naturalistic slow-motion feeling."
)


def generate_motion_prompt(scene: str, config: Optional[Config] = None) -> str:
    """Turn a visual scene description into a detailed i2v motion prompt.

    Args:
        scene: The scene's image-generation description.
        config: Configuration instance.

    Returns:
        A motion prompt describing slow, restrained, realistic movement,
        with a fixed negative-prompt tail appended.
    """
    config = config or get_config()

    fallback_body = (
        f"{scene}. Subtle, restrained natural motion within the frame — gentle "
        f"breathing, minimal environmental movement, and an almost imperceptible "
        f"slow camera push-in. Maintain the original framing, lighting, and depth "
        f"of field throughout."
    )

    if not config.has_llm:
        return f"{fallback_body} {_MOTION_NEGATIVE_TAIL}"

    prompt = f"""Write a short motion description (100-160 words) for an image-to-video AI model, based on this visual scene:

"{scene}"

Rules:
- Describe only slow, restrained, psychologically realistic motion — subtle body language, breathing, environmental movement, or a slow camera push-in/pan
- Never describe dramatic action, fast movement, or scene changes
- Keep the original composition, framing, subject positioning, lighting, and depth of field consistent throughout
- Write it as a single flowing paragraph, present tense
- Do not include any disclaimers or negative instructions — just describe the motion itself

Return ONLY the motion description paragraph, nothing else."""

    try:
        text = _call_llm(prompt, config, max_tokens=400, temperature=0.7).strip()
        if text:
            return f"{text} {_MOTION_NEGATIVE_TAIL}"
    except RuntimeError as exc:
        log.warning("Motion prompt generation failed: %s", exc)

    return f"{fallback_body} {_MOTION_NEGATIVE_TAIL}"


# ── AI image generation ──────────────────────────────────────────────────────


def generate_image(
    prompt: str,
    output_path: Path,
    config: Optional[Config] = None,
) -> Path:
    """Generate a portrait image via Replicate's Flux Schnell.

    Args:
        prompt: Image generation prompt.
        output_path: Where to save the PNG image.
        config: Configuration instance.

    Returns:
        The output_path on success.

    Raises:
        RuntimeError: If REPLICATE_API_TOKEN is not set or generation fails.
    """
    import httpx
    import replicate

    config = config or get_config()

    if not config.has_replicate:
        raise RuntimeError(
            "CLIPFORGE_REPLICATE_KEY / REPLICATE_API_TOKEN not set — cannot generate AI images"
        )

    client = replicate.Client(
        api_token=config.replicate_key,
        timeout=httpx.Timeout(10.0, read=120.0, connect=10.0, pool=10.0),
    )
    enhanced = _enhance_prompt(prompt)
    log.info("Generating image: %s...", prompt[:60])

    outputs = client.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": enhanced,
            "aspect_ratio": "9:16",
            "num_outputs": 1,
            "output_format": "png",
            "disable_safety_checker": True,
        },
    )

    if not outputs:
        raise RuntimeError("Replicate returned no images")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(outputs[0].read())

    size_kb = output_path.stat().st_size // 1024
    log.info("Saved image: %s (%d KB)", output_path.name, size_kb)
    return output_path


def _reword_scene_prompt(prompt: str, config: Config) -> str:
    """Ask the LLM to rephrase a scene prompt that failed to generate.

    Keeps the same subject, setting, and mood but changes the wording —
    useful when a generation failure is caused by specific phrasing
    (e.g. a content-filter trigger) rather than the scene itself.
    """
    if not config.has_llm:
        return prompt

    llm_prompt = f"""This AI image generation prompt failed to produce a result:

"{prompt}"

Rewrite it to describe the exact same scene, subject, and mood, but using
different wording and phrasing — in case specific words triggered the
failure. Keep the same length and level of visual detail.

Return ONLY the rewritten prompt, nothing else."""

    try:
        text = _call_llm(llm_prompt, config, max_tokens=200, temperature=0.9).strip()
        if text:
            return text
    except RuntimeError as exc:
        log.warning("Prompt reword failed: %s", exc)

    return prompt


def generate_image_with_retry(
    prompt: str,
    output_path: Path,
    config: Optional[Config] = None,
    max_attempts: int = 5,
) -> Path:
    """Generate an image, retrying on failure and rewording the prompt via LLM
    if repeated attempts with the original wording keep failing.

    Args:
        prompt: Image generation prompt.
        output_path: Where to save the PNG image.
        config: Configuration instance.
        max_attempts: Total attempts before giving up (no gradient fallback).

    Returns:
        The output_path on success.

    Raises:
        RuntimeError: If all attempts are exhausted.
    """
    config = config or get_config()
    current_prompt = prompt
    last_exc: Optional[Exception] = None

    for attempt in range(1, max_attempts + 1):
        try:
            return generate_image(current_prompt, output_path, config=config)
        except Exception as exc:
            last_exc = exc
            log.warning(
                "Image generation attempt %d/%d failed: %s", attempt, max_attempts, exc
            )
            if attempt >= 2 and attempt < max_attempts:
                current_prompt = _reword_scene_prompt(current_prompt, config)
                log.info("Rewording prompt after failure: %s...", current_prompt[:60])

    raise RuntimeError(
        f"Image generation failed after {max_attempts} attempts: {last_exc}"
    )


# ── Image-to-video animation ─────────────────────────────────────────────────


def generate_i2v_clip(
    image_path: Path,
    motion_prompt: str,
    output_path: Path,
    duration: int = 5,
    config: Optional[Config] = None,
) -> Path:
    """Animate a still image into a motion clip via Replicate's image-to-video model.

    Args:
        image_path: Path to the source image (used as the first frame).
        motion_prompt: Detailed motion/camera description for the model.
        output_path: Where to save the MP4 clip.
        duration: Clip duration in seconds (1-20).
        config: Configuration instance.

    Returns:
        The output_path on success.

    Raises:
        RuntimeError: If REPLICATE_API_TOKEN is not set or generation fails.
    """
    import httpx
    import replicate

    config = config or get_config()

    if not config.has_replicate:
        raise RuntimeError(
            "CLIPFORGE_REPLICATE_KEY / REPLICATE_API_TOKEN not set — cannot generate i2v clips"
        )

    client = replicate.Client(
        api_token=config.replicate_key,
        timeout=httpx.Timeout(10.0, read=180.0, connect=10.0, pool=10.0),
    )

    with open(image_path, "rb") as img_file:
        output = client.run(
            "prunaai/p-video",
            input={
                "prompt": motion_prompt,
                "image": img_file,
                "duration": duration,
                "resolution": "720p",
                "fps": 24,
                "draft": False,
                "prompt_upsampling": True,
                "disable_safety_filter": True,
            },
        )

    if not output:
        raise RuntimeError("Replicate returned no i2v output")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # p-video returns 704x1280@24fps — normalize to the pipeline's standard
    # 1080x1920@30fps so concat doesn't choke on mismatched stream params
    # (mixed fps/resolution inputs cause frozen/repeated-frame glitches).
    raw_path = output_path.with_suffix(".raw.mp4")
    raw_path.write_bytes(output.read())

    cmd = [
        "ffmpeg", "-y",
        "-i", str(raw_path),
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "fast", "-crf", "20",
        "-an",
        str(output_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    raw_path.unlink(missing_ok=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg i2v normalization failed: {result.stderr[-500:]}")

    size_kb = output_path.stat().st_size // 1024
    log.info("Saved i2v clip: %s (%d KB, %ds)", output_path.name, size_kb, duration)
    return output_path


# ── Clip duration fitting ────────────────────────────────────────────────────


def _probe_duration(path: Path) -> float:
    """Return a media file's duration in seconds via ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def _fit_clip_duration(
    clip_path: Path,
    target_duration: float,
    tolerance: float = 0.15,
) -> None:
    """Trim or pad (by holding the last frame) a clip in place to match
    ``target_duration`` exactly.

    i2v clips are requested at an integer-rounded duration and the model's
    actual output can drift slightly, so this is what guarantees every clip
    handed to compose_video is exactly as long as the narration segment it's
    supposed to be on screen for.
    """
    actual = _probe_duration(clip_path)
    diff = target_duration - actual
    if actual <= 0 or abs(diff) <= tolerance:
        return

    tmp_path = clip_path.with_suffix(".fit.mp4")
    if diff < 0:
        cmd = [
            "ffmpeg", "-y", "-i", str(clip_path),
            "-t", f"{target_duration:.3f}",
            "-c", "copy",
            str(tmp_path),
        ]
    else:
        cmd = [
            "ffmpeg", "-y", "-i", str(clip_path),
            "-vf", f"tpad=stop_mode=clone:stop_duration={diff:.3f}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-preset", "fast", "-crf", "20",
            "-an",
            str(tmp_path),
        ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0 or not tmp_path.exists():
        log.warning("Duration fit failed for %s: %s", clip_path.name, result.stderr[-300:])
        tmp_path.unlink(missing_ok=True)
        return
    tmp_path.replace(clip_path)


# ── Ken Burns effect ─────────────────────────────────────────────────────────


def image_to_clip(
    image_path: Path,
    output_path: Path,
    duration: float = 5.0,
) -> Path:
    """Convert a static image to a video clip with Ken Burns zoom/pan effect.

    Args:
        image_path: Path to the source image.
        output_path: Where to save the MP4 clip.
        duration: Clip duration in seconds.

    Returns:
        The output_path on success.

    Raises:
        RuntimeError: If ffmpeg fails.
    """
    fps = 30
    total_frames = int(duration * fps)

    effect = random.choice(["zoom_in", "zoom_out", "pan_right", "pan_left"])

    # Work at 2x resolution internally for smooth sub-pixel movement,
    # then downscale to 1080x1920 at the end.
    canvas_w, canvas_h = 2160, 3840

    # Slow, smooth movements — smaller increments prevent jitter
    zoom_step = 0.0005  # very gradual zoom
    pan_step = 1        # 1px at 2x res = 0.5px at output

    zoompan_filters = {
        "zoom_in": (
            f"zoompan=z='min(zoom+{zoom_step},1.12)'"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s={canvas_w}x{canvas_h}:fps={fps}"
        ),
        "zoom_out": (
            f"zoompan=z='if(eq(on,1),1.12,max(zoom-{zoom_step},1.0))'"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s={canvas_w}x{canvas_h}:fps={fps}"
        ),
        "pan_right": (
            f"zoompan=z='1.08'"
            f":x='if(eq(on,1),0,min(x+{pan_step},iw-iw/zoom))'"
            f":y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s={canvas_w}x{canvas_h}:fps={fps}"
        ),
        "pan_left": (
            f"zoompan=z='1.08'"
            f":x='if(eq(on,1),iw-iw/zoom,max(x-{pan_step},0))'"
            f":y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s={canvas_w}x{canvas_h}:fps={fps}"
        ),
    }

    zoompan = zoompan_filters[effect]
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Upscale image first for clean zoompan, then downscale to 1080x1920
    vf = f"scale=2160:3840:flags=lanczos,{zoompan},scale=1080:1920:flags=lanczos"

    cmd = [
        "nice", "-n", "15", "ffmpeg", "-y",
        "-loop", "1", "-i", str(image_path),
        "-vf", vf,
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "fast", "-crf", "20",
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg zoompan failed: {result.stderr[-500:]}")

    log.info("Ken Burns clip: %s (%.1fs, %s)", output_path.name, duration, effect)
    return output_path


# ── Fallback gradient clip ───────────────────────────────────────────────────


def _generate_gradient_clip(output_path: Path, duration: float = 5.0) -> Path:
    """Generate a solid gradient color clip as fallback when no REPLICATE_API_TOKEN."""
    c0, c1 = random.choice(GRADIENT_PALETTES)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i",
        f"color=c={c0}:s=1080x1920:d={duration}:r=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "fast", "-crf", "23",
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg gradient clip failed: {result.stderr[-500:]}")

    log.info("Gradient clip: %s (%.1fs)", output_path.name, duration)
    return output_path


# ── Main orchestrator ────────────────────────────────────────────────────────


def _process_scene(
    index: int,
    seg: dict,
    output_dir: Path,
    use_ai: bool,
    keep_images: bool,
    num_segments: int,
    config: Config,
    cancel_event: Optional[threading.Event],
) -> Path:
    """Generate one scene's clip. Runs inside a worker thread — see
    ``MAX_CONCURRENT_SCENES`` — so it tags this thread's log records with
    its scene index before doing anything else."""
    _scene_context.index = index

    if cancel_event is not None and cancel_event.is_set():
        raise GenerationCancelled(f"Cancelled before scene {index + 1}/{num_segments}")

    duration = seg["duration"]
    uid = uuid.uuid4().hex[:6]

    if use_ai:
        # Image generation: retries + LLM prompt rewording, no gradient
        # fallback — a persistent failure here raises and aborts the run.
        prompt = seg["prompt"]
        img_path = output_dir / f"ai_img_{index:02d}_{uid}.png"
        clip_path = output_dir / f"ai_clip_{index:02d}_{uid}.mp4"

        generate_image_with_retry(prompt, img_path, config=config)

        i2v_duration = max(2, min(20, round(duration)))
        try:
            motion_prompt = generate_motion_prompt(prompt, config=config)
            generate_i2v_clip(
                img_path, motion_prompt, clip_path,
                duration=i2v_duration, config=config,
            )
        except Exception as exc:
            log.warning(
                "i2v generation failed for scene %d: %s — using Ken Burns fallback",
                index + 1, exc,
            )
            image_to_clip(img_path, clip_path, duration=duration)

        if not keep_images:
            img_path.unlink(missing_ok=True)
        _fit_clip_duration(clip_path, duration)
        log.info(
            "Scene %d/%d: AI generated (%.1fs, %.1f-%.1fs in narration)",
            index + 1, num_segments, duration, seg["start"], seg["end"],
        )
        return clip_path

    # AI disabled entirely (no Replicate token) — gradient for every scene.
    clip_path = output_dir / f"gradient_clip_{index:02d}_{uid}.mp4"
    _generate_gradient_clip(clip_path, duration=duration)
    _fit_clip_duration(clip_path, duration)
    log.info("Scene %d/%d: gradient fallback (%.1fs)", index + 1, num_segments, duration)
    return clip_path


def generate_clips(
    story: str,
    output_dir: Path,
    word_data: list[dict],
    config: Optional[Config] = None,
    keep_images: bool = False,
    cancel_event: Optional[threading.Event] = None,
) -> list[Path]:
    """Generate visual clips aligned to the story's actual narration timing.

    Splits the story into scenes at natural sentence boundaries (roughly one
    every ``TARGET_SCENE_SECONDS``, derived from the real narrated audio
    duration), computes each scene's exact on-screen window from the TTS
    word timestamps, and generates a clip trimmed/padded to that exact
    duration — so clip N is guaranteed to be on screen for exactly as long
    as its corresponding narration is being spoken.

    Up to ``MAX_CONCURRENT_SCENES`` scenes generate concurrently (bounded to
    avoid tripping Replicate's per-minute rate limit on low-credit accounts).
    Image generation retries and rewords the prompt via LLM on repeated
    failure rather than falling back — a persistent failure aborts the run.
    Falls back to a Ken Burns zoom/pan clip if only the i2v step fails, and
    to a solid gradient clip only when no Replicate token is configured.

    Args:
        story: The narrated story text.
        output_dir: Directory to save generated clips.
        word_data: TTS word-timestamp list from ``voice.generate_speech``.
        config: Configuration instance.
        keep_images: If True, don't delete the generated still image after
            animating it (e.g. so a caller can offer an image preview).
        cancel_event: If set, no scene that hasn't already started its
            image/i2v calls will start — but an in-flight scene still
            finishes (can't interrupt a live network call). Since scenes run
            concurrently, up to ``MAX_CONCURRENT_SCENES`` may finish before
            the run actually stops, not just one as in a sequential loop.

    Returns:
        Ordered list of clip paths (MP4) in original scene order regardless
        of completion order, each fit to its scene's exact narrated duration.

    Raises:
        GenerationCancelled: If ``cancel_event`` was set before a scene
            could start.
    """
    config = config or get_config()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_duration = (
        word_data[-1]["start"] + word_data[-1]["duration"] if word_data else 60.0
    )
    target_scene_count = max(3, round(audio_duration / TARGET_SCENE_SECONDS))

    sentences = _split_sentences(story)
    use_ai = config.has_replicate

    segments = segment_story_into_scenes(story, target_scene_count, config=config)
    segments = compute_scene_timings(segments, sentences, word_data)
    segments = split_long_segments(segments, max_duration=TARGET_SCENE_SECONDS * 2)
    log.info(
        "Segmented story into %d scenes from %d sentences",
        len(segments), len(sentences),
    )

    clips: list[Optional[Path]] = [None] * len(segments)
    first_exc: Optional[BaseException] = None

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_SCENES) as executor:
        futures = {
            executor.submit(
                _process_scene, i, seg, output_dir, use_ai, keep_images,
                len(segments), config, cancel_event,
            ): i
            for i, seg in enumerate(segments)
        }
        for future in concurrent.futures.as_completed(futures):
            try:
                clips[futures[future]] = future.result()
            except Exception as exc:
                if first_exc is None:
                    first_exc = exc
                # Don't start scenes that haven't already begun.
                for f in futures:
                    f.cancel()

    if first_exc is not None:
        raise first_exc

    clips_final = [c for c in clips if c is not None]
    ai_count = sum(1 for c in clips_final if "ai_clip" in c.name)
    log.info("Generated %d AI + %d fallback clips", ai_count, len(clips_final) - ai_count)
    return clips_final
