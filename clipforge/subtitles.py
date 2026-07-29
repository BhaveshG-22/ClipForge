"""
ASS subtitle generation for clipforge.

Creates word-by-word highlighted subtitles in ASS format with
Montserrat Bold 58px, white text with yellow highlight on the
current word. The single "punchiest" word per caption group (a number,
or the longest non-stopword) gets a distinct accent color plus a quick
scale-pop animation instead of the plain yellow highlight. Positioned
center-bottom for vertical (9:16) video.
"""

import logging
from pathlib import Path
from typing import Optional

log = logging.getLogger("clipforge.subtitles")

# Common low-information words — skipped when picking which word in a
# caption group gets the emphasis treatment (numbers always win regardless).
_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being", "to",
    "of", "in", "on", "at", "and", "but", "or", "for", "with", "as", "that",
    "this", "it", "its", "you", "your", "i", "we", "they", "he", "she",
    "them", "his", "her", "our", "us", "my", "me", "so", "if", "not", "no",
    "do", "does", "did", "have", "has", "had", "will", "would", "can",
    "could", "should", "just", "than", "then", "there", "here", "from",
    "by", "about", "into", "over", "out", "up", "down", "off", "again",
    "once", "when", "where", "why", "how", "what", "who", "which", "all",
    "each", "few", "more", "most", "other", "some", "such", "only", "own",
    "same", "too", "very", "s", "t", "don", "now",
}


def _pick_emphasis_index(chunk: list[dict]) -> Optional[int]:
    """Pick the single most 'punchy' word in a caption group to emphasize.

    Numbers win outright (they're the highest-information tokens in a
    stats/facts script). Otherwise, the longest word that isn't a common
    stopword is picked — a cheap stand-in for "this is the word carrying
    the sentence's meaning" without needing an extra LLM call per video.
    """
    for i, w in enumerate(chunk):
        if any(ch.isdigit() for ch in w["text"]):
            return i

    best_i: Optional[int] = None
    best_len = 0
    for i, w in enumerate(chunk):
        clean = w["text"].strip(".,!?;:\"'").lower()
        if clean in _STOPWORDS or len(clean) < 4:
            continue
        if len(clean) > best_len:
            best_i, best_len = i, len(clean)
    return best_i

# ── ASS header template ──────────────────────────────────────────────────────

ASS_HEADER = """\
[Script Info]
Title: clipforge
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Default,Montserrat Bold,58,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,2,0,1,3,2,2,40,40,120,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""


def _format_timestamp(seconds: float) -> str:
    """Format seconds as ASS timestamp ``H:MM:SS.cc``."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


# ── Public API ───────────────────────────────────────────────────────────────


def generate_subtitles(
    word_data: list[dict],
    output_path: Path,
    words_per_group: int = 3,
) -> Path:
    """Generate an ASS subtitle file with word-by-word yellow highlighting.

    Each group of ``words_per_group`` words is displayed together. Within
    each group, the current word is highlighted in yellow while the rest
    remain white, creating a karaoke-style reading effect.

    Args:
        word_data: List of dicts from ``voice.generate_speech``, each with
            ``text`` (str), ``start`` (float seconds), ``duration`` (float).
        output_path: Where to write the ``.ass`` file.
        words_per_group: How many words to show at once (default 3).

    Returns:
        The output_path.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Group words into display chunks
    groups: list[dict] = []
    for i in range(0, len(word_data), words_per_group):
        chunk = word_data[i : i + words_per_group]
        text = " ".join(w["text"] for w in chunk).upper()
        start = chunk[0]["start"]
        end = chunk[-1]["start"] + chunk[-1]["duration"]
        groups.append({"text": text, "start": start, "end": end, "words": chunk})

    # Build ASS dialogue lines
    lines: list[str] = []

    for g_idx, group in enumerate(groups):
        chunk = group["words"]
        words_upper = [w["text"].upper() for w in chunk]
        emphasis_idx = _pick_emphasis_index(chunk)

        for w_idx, word in enumerate(chunk):
            w_start = word["start"]
            w_end = word["start"] + word["duration"]

            # Extend timing for seamless display
            if w_idx < len(chunk) - 1:
                w_end = chunk[w_idx + 1]["start"]
            elif g_idx < len(groups) - 1:
                w_end = group["end"]

            # Build text with current word highlighted yellow, or — for the
            # group's single "punchiest" word — a distinct accent color plus
            # a quick scale-pop so it visually pops off the rest of the line.
            parts: list[str] = []
            for j, word_text in enumerate(words_upper):
                if j == w_idx and j == emphasis_idx:
                    parts.append(
                        r"{\c&H00457AFF&\fscx100\fscy100"
                        r"\t(0,120,\fscx135\fscy135)\t(120,260,\fscx100\fscy100)}"
                        + word_text
                        + r"{\c&H00FFFFFF&\fscx100\fscy100}"
                    )
                elif j == w_idx:
                    # Yellow highlight: &H0000FFFF = AABBGGRR = yellow
                    parts.append(
                        r"{\c&H0000FFFF&}" + word_text + r"{\c&H00FFFFFF&}"
                    )
                else:
                    parts.append(word_text)

            line_text = r"{\an2}" + " ".join(parts)
            ts_start = _format_timestamp(w_start)
            ts_end = _format_timestamp(w_end)

            lines.append(
                f"Dialogue: 0,{ts_start},{ts_end},Default,,0,0,0,,{line_text}"
            )

    # Write ASS file
    ass_content = ASS_HEADER + "\n".join(lines) + "\n"
    output_path.write_text(ass_content, encoding="utf-8")

    log.info(
        "Subtitles generated: %s (%d groups, %d events)",
        output_path.name, len(groups), len(lines),
    )
    return output_path
