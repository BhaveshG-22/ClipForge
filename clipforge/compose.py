"""
FFmpeg video composition for clipforge.

Concatenates video clips, mixes voice + optional background music,
burns in ASS subtitles, and outputs a 1080x1920 H.264 MP4 ready
for YouTube Shorts / TikTok.
"""

import json
import logging
import subprocess
from pathlib import Path
from typing import Optional

log = logging.getLogger("clipforge.compose")


def _get_duration(media_path: Path) -> float:
    """Probe a media file and return its duration in seconds."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "json",
        str(media_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed on {media_path}: {result.stderr[-300:]}")
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def compose_video(
    clips: list[Path],
    audio: Path,
    subs: Path,
    output: Path,
    music: Optional[Path] = None,
    voice_vol: float = 0.85,
    music_vol: float = 0.08,
) -> Path:
    """Compose the final short-form video.

    Concatenates clips (straight cuts, no transitions), scales to 1080x1920
    with crop (no black bars), mixes voice audio with optional background
    music, and burns in ASS subtitles.

    Args:
        clips: Ordered list of video clip paths, each already fit to its
            scene's exact narrated duration by visuals.generate_clips.
        audio: Path to the voice narration audio file.
        subs: Path to the ASS subtitle file.
        output: Where to save the final MP4.
        music: Optional background music file (will be looped and mixed).
        voice_vol: Voice volume multiplier (default 0.85).
        music_vol: Music volume multiplier (default 0.08).

    Returns:
        The output path on success.

    Raises:
        RuntimeError: If ffmpeg fails or no clips are provided.
    """
    if not clips:
        raise RuntimeError("No video clips provided for composition")

    clips = [Path(c) for c in clips]
    audio = Path(audio)
    subs = Path(subs)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    audio_dur = _get_duration(audio)
    duration = audio_dur + 1.0  # 1s padding

    log.info(
        "Composing video: %d clips, %.1fs audio, output=%s",
        len(clips), audio_dur, output.name,
    )

    subs_escaped = (
        str(subs.resolve())
        .replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\\'")
    )
    base_vf = (
        f"scale=1080:1920:force_original_aspect_ratio=increase,"
        f"crop=1080:1920,"
        f"ass={subs_escaped}"
    )

    cmd = ["ffmpeg", "-y"]
    for clip in clips:
        cmd += ["-i", str(clip.resolve())]
    audio_idx = len(clips)
    cmd += ["-i", str(audio)]

    music_idx = None
    if music:
        music_idx = len(clips) + 1
        cmd += ["-stream_loop", "-1", "-i", str(music)]

    cmd += ["-t", str(duration)]

    if len(clips) == 1:
        video_filters = f"[0:v]{base_vf}[vout]"
    else:
        concat_inputs = "".join(f"[{i}:v]" for i in range(len(clips)))
        video_filters = (
            f"{concat_inputs}concat=n={len(clips)}:v=1:a=0[vconcat];"
            f"[vconcat]{base_vf}[vout]"
        )

    if music:
        filter_complex = (
            f"{video_filters};"
            f"[{audio_idx}:a]volume={voice_vol}[voice];"
            f"[{music_idx}:a]volume={music_vol}[music];"
            f"[voice][music]amix=inputs=2:duration=first[aout]"
        )
    else:
        filter_complex = f"{video_filters};[{audio_idx}:a]volume={voice_vol}[aout]"

    cmd += [
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", "[aout]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        "-movflags", "+faststart",
        "-r", "30",
        "-pix_fmt", "yuv420p",
        str(output),
    ]

    log.debug("FFmpeg command: %s", " ".join(cmd))
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

    if proc.returncode != 0:
        raise RuntimeError(f"FFmpeg failed: {proc.stderr[-500:]}")

    size_mb = output.stat().st_size / 1024 / 1024
    log.info("Video composed: %s (%.1f MB, %.1fs)", output.name, size_mb, duration)
    return output
