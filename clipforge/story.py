"""
Story generation for clipforge.

Generates engaging 140-165 word short-form video scripts via any
OpenAI-compatible LLM (Groq free tier, OpenAI, Anthropic).
Supports 11 content styles and 25+ hook templates.
"""

import dataclasses
import json
import logging
import random
import re
import time
import requests as _requests
from typing import Optional

from .config import Config, get_config

log = logging.getLogger("clipforge.story")

# ── Content styles ───────────────────────────────────────────────────────────

STYLES: dict[str, str] = {
    "mind_blowing": (
        "Tell a mind-blowing scientific or historical fact that most people "
        "don't know. Tone: amazed, wonder."
    ),
    "dark_fact": (
        "Tell a dark, mysterious, little-known fact. The tone should be calm, "
        "mysterious, almost whispered."
    ),
    "psychology": (
        "Tell a disturbing or fascinating psychology fact about human behavior. "
        "Tone: intimate, thought-provoking."
    ),
    "space": (
        "Tell an awe-inspiring fact about space or the universe. "
        "Tone: grand, contemplative."
    ),
    "nature": (
        "Tell an incredible fact about nature or animals. "
        "Tone: warm, contemplative, awe-inspiring."
    ),
    "history": (
        "Tell a forgotten or bizarre historical story. "
        "Tone: storytelling, dramatic."
    ),
    "ocean_deep": (
        "Tell an incredible fact about the deep ocean or sea creatures. "
        "Tone: mysterious, awe-inspiring, slightly terrifying."
    ),
    "future_tech": (
        "Tell a mind-bending fact about emerging technology or what science "
        "says the future holds. Tone: excited, visionary."
    ),
    "body_facts": (
        "Tell a bizarre fact about the human body that makes people go wow. "
        "Tone: intimate, slightly gross, fascinating."
    ),
    "myth_busted": (
        "Debunk a common myth or misconception that most people believe. "
        "Tone: confident, revelatory, slightly smug."
    ),
    "food_origins": (
        "Tell a surprising origin story about a common food or drink. "
        "Tone: conversational, surprising."
    ),
}

# ── Hook templates ───────────────────────────────────────────────────────────

HOOK_TEMPLATES: list[str] = [
    # DIRECT SHOCK
    "Open with the most shocking detail of the story as a bold statement. No intro.",
    "Start with a specific number or statistic that sounds impossible.",
    "State something terrifying as casually as possible, like it's common knowledge.",
    # CURIOSITY GAP
    "Start with 'Nobody talks about this, but...' and reveal something unsettling.",
    "Start with 'There's a reason why...' to create instant curiosity.",
    "Start with 'You've been told [common belief]. That's not exactly true.'",
    "Start with 'Here's something that was hidden for decades.'",
    "Start with 'Everyone assumes [X]. The truth is far stranger.'",
    # SCENE SETTING
    "Start with 'Picture this:' followed by a vivid scene that pulls the listener in.",
    "Start with a specific date, place, and action — like a documentary opening.",
    "Start with 'Right now, as you listen to this...' to create immediacy.",
    "Start with a sensory detail — what you'd smell, hear, or feel in the scene.",
    # QUESTION / CHALLENGE
    "Start with 'Have you ever noticed...' followed by something eerie.",
    "Start with 'Ever wonder why...' and then reveal something disturbing.",
    "Start with 'Can you guess what...' followed by a mind-bending fact.",
    "Start with 'Think about the last time you...' to make it personal.",
    # REVELATION
    "Start with 'Scientists still can't explain why...'",
    "Start with 'In [year], something happened that changed everything.'",
    "Start with 'The scariest part? This is completely real.'",
    "Start with 'Most people walk past this every day without knowing...'",
    "Start with 'This story was buried for years.'",
    # SECRET / FORBIDDEN
    "Start with 'This is the story they tried to erase.'",
    "Start with 'Behind closed doors, something happened that...'",
    "Start with 'There is a place where...' and describe something uncanny.",
    # VIRAL PATTERNS
    "Start mid-story as if the viewer dropped into an ongoing conversation.",
    "Start with THE most unbelievable detail, then say 'Let me back up...'",
    "Start with 'This is going to sound fake, but...'",
    "Start with 'POV:' followed by a scenario.",
    "Start with a one-word sentence for maximum impact, then expand.",
]

# ── Banned phrases ───────────────────────────────────────────────────────────

BANNED_PHRASES: list[str] = [
    "What if I told you",
    "What if I said",
    "Let me tell you",
    "Did you know",
    "Brace yourself",
    "Buckle up",
    "Here is the thing",
    "Here's the thing",
    "You won't believe",
    "Gather round",
    "Gather around",
    "Sit down for this",
]

_BANNED_RE = re.compile(
    r"^(" + "|".join(re.escape(p) for p in BANNED_PHRASES) + r")\b",
    re.IGNORECASE,
)


def _filter_banned(story: str) -> str:
    """Remove banned opener phrases from the story."""
    cleaned = _BANNED_RE.sub("", story).lstrip(" ,.:;—-")
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned


_STORY_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_MAX_STORY_SENTENCE_WORDS = 20


def _break_long_sentences(story: str, max_words: int = _MAX_STORY_SENTENCE_WORDS) -> str:
    """Deterministically split any sentence over ``max_words`` at its most
    balanced comma boundary.

    The prompt asks for a hard per-sentence word cap, but LLMs don't
    reliably obey hard caps every single time — especially on the final
    "big finish" line, where the model tends to chain several clauses
    together for dramatic effect. This is a safety net that runs after
    generation so an occasional non-compliant sentence never reaches the
    viewer as an unbroken run-on: harder to follow when read aloud, and
    (upstream in the visuals pipeline) harder to fit into a short scene.
    """
    sentences = [s for s in _STORY_SENTENCE_RE.split(story.strip()) if s]

    def split_one(sentence: str) -> list[str]:
        words = sentence.split()
        if len(words) <= max_words:
            return [sentence]

        comma_positions = [i + 1 for i, w in enumerate(words[:-1]) if w.endswith(",")]
        if not comma_positions:
            return [sentence]

        mid = len(words) / 2
        split_at = min(comma_positions, key=lambda p: abs(p - mid))
        if split_at <= 1 or split_at >= len(words) - 1:
            return [sentence]

        first_words = words[:split_at]
        first_words[-1] = first_words[-1].rstrip(",") + "."
        second_words = words[split_at:]
        second_words[0] = second_words[0][0].upper() + second_words[0][1:]

        return split_one(" ".join(first_words)) + split_one(" ".join(second_words))

    out: list[str] = []
    for sentence in sentences:
        out.extend(split_one(sentence))
    return " ".join(out)


# ── LLM call ─────────────────────────────────────────────────────────────────


def _call_llm(
    prompt: str,
    config: Config,
    max_tokens: int = 1200,
    temperature: float = 0.8,
) -> str:
    """Send a chat completion request to the configured LLM provider.

    1200 (not 800) is the default floor because some Replicate-hosted
    models (e.g. Claude via ``anthropic/claude-4-sonnet``) reject anything
    below 1024 outright.
    """
    if not config.has_llm:
        raise RuntimeError(
            "No LLM API key configured. Set CLIPFORGE_LLM_KEY or pass it in config."
        )

    provider = config.llm_provider

    if provider == "anthropic":
        return _call_anthropic(prompt, config, max_tokens, temperature)

    if provider == "replicate":
        return _call_replicate_llm(prompt, config, max_tokens, temperature)

    # OpenAI-compatible (Groq, OpenAI)
    payload = {
        "model": config.resolved_model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    headers = {
        "Authorization": f"Bearer {config.llm_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(3):
        try:
            resp = _requests.post(
                config.llm_endpoint,
                headers=headers,
                json=payload,
                timeout=60,
            )
            if resp.status_code == 429 and attempt < 2:
                wait = 2 ** attempt * 3
                log.warning("Rate limited (429), waiting %ds...", wait)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            result = resp.json()
            return result["choices"][0]["message"]["content"].strip()
        except _requests.exceptions.HTTPError as exc:
            body = resp.text[:300] if resp is not None else str(exc)
            raise RuntimeError(f"LLM API error {resp.status_code}: {body}") from exc
        except Exception as exc:
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"LLM request failed: {exc}") from exc

    raise RuntimeError("LLM: max retries exceeded")


def _call_anthropic(
    prompt: str,
    config: Config,
    max_tokens: int,
    temperature: float,
) -> str:
    """Call the Anthropic Messages API."""
    payload = {
        "model": config.resolved_model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }

    headers = {
        "x-api-key": config.llm_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }

    for attempt in range(3):
        try:
            resp = _requests.post(
                config.llm_endpoint,
                headers=headers,
                json=payload,
                timeout=60,
            )
            if resp.status_code == 429 and attempt < 2:
                time.sleep(2 ** attempt * 3)
                continue
            resp.raise_for_status()
            result = resp.json()
            return result["content"][0]["text"].strip()
        except _requests.exceptions.HTTPError as exc:
            body = resp.text[:300] if resp is not None else str(exc)
            raise RuntimeError(f"Anthropic API error {resp.status_code}: {body}") from exc
        except Exception as exc:
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"Anthropic request failed: {exc}") from exc

    raise RuntimeError("Anthropic: max retries exceeded")


def _call_replicate_llm(
    prompt: str,
    config: Config,
    max_tokens: int,
    temperature: float,
) -> str:
    """Call an LLM hosted on Replicate.

    Covers two shapes: open-weight prompt-completion models (gpt-oss) that
    take ``prompt``/``max_tokens``/``temperature``/``top_p``, and officially
    hosted chat models under their vendor's own namespace (``anthropic/``,
    ``openai/``) whose input schemas differ per vendor and don't accept a
    raw ``temperature``/``top_p`` pair.
    """
    import httpx
    import replicate

    client = replicate.Client(
        api_token=config.replicate_key,
        timeout=httpx.Timeout(10.0, read=180.0, connect=10.0, pool=10.0),
    )

    model = config.resolved_model
    if model.startswith("anthropic/"):
        model_input = {"prompt": prompt, "max_tokens": max_tokens}
    elif model.startswith("openai/"):
        model_input = {"prompt": prompt, "max_completion_tokens": max_tokens}
    else:
        model_input = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": 1,
        }

    for attempt in range(3):
        try:
            output = client.run(model, input=model_input)
            return "".join(output).strip()
        except Exception as exc:
            if attempt < 2:
                time.sleep(2 ** attempt * 3)
                continue
            raise RuntimeError(f"Replicate LLM request failed: {exc}") from exc

    raise RuntimeError("Replicate LLM: max retries exceeded")


# ── Public API ───────────────────────────────────────────────────────────────


# Calibrated from real TTS runs (Edge TTS, -8% rate): ~2.5 words/sec.
WORDS_PER_SECOND = 2.5


def generate_story(
    style: str = "mind_blowing",
    topic: Optional[str] = None,
    target_seconds: float = 60.0,
    config: Optional[Config] = None,
    llm_provider: Optional[str] = None,
    llm_model: Optional[str] = None,
) -> str:
    """Generate an engaging short-form video script.

    Args:
        style: Content style key (see ``STYLES``).
        topic: Optional topic hint to guide the story.
        target_seconds: Desired narration length in seconds; the word count
            band is derived from this (~2.5 words/sec).
        config: Configuration instance. Uses env vars if not provided.
        llm_provider: Which provider generates the script. Defaults to
            ``config.script_llm_provider`` (itself defaulting to Groq — a
            free, reliable chat-completion API) when not passed explicitly.
            gpt-oss-120b via Replicate's raw-prompt mode has been observed
            to truncate mid-sentence for some prompts (it expects the
            "harmony" response format, not a bare prompt string), so don't
            point this at Replicate without also setting ``llm_model`` to a
            model that accepts plain prompts (e.g. an ``anthropic/`` or
            ``openai/`` model hosted there).
        llm_model: Explicit model override for ``llm_provider``. Defaults
            to ``config.script_llm_model`` (e.g.
            ``"anthropic/claude-4-sonnet"`` when the provider is
            ``"replicate"``).

    Returns:
        A story script sized for roughly ``target_seconds`` of narration.

    Raises:
        RuntimeError: If the LLM call fails.
        ValueError: If the style is unknown.
    """
    config = config or get_config()
    llm_provider = llm_provider if llm_provider is not None else config.script_llm_provider
    llm_model = llm_model if llm_model is not None else config.script_llm_model

    if style not in STYLES:
        available = ", ".join(sorted(STYLES.keys()))
        raise ValueError(f"Unknown style '{style}'. Available: {available}")

    target_words = round(target_seconds * WORDS_PER_SECOND)
    low_words = max(20, target_words - 12)
    high_words = target_words + 12
    min_acceptable_words = max(20, int(low_words * 0.6))

    style_prompt = STYLES[style]
    hook_instruction = random.choice(HOOK_TEMPLATES)
    topic_hint = f" The topic should be related to: {topic}." if topic else ""

    prompt = f"""You are a retention-focused scriptwriter for a faceless short-form video channel (TikTok/YouTube Shorts).

CHANNEL NICHE: {style_prompt}{topic_hint}
LENGTH: ~{target_seconds:.0f} seconds of narration, {low_words}-{high_words} words. Count carefully — too short kills the pacing, too long loses viewers
FORMAT: Shorts — one continuous piece of narration, no scene headers, no labels

HOOK (first sentence only — the first ~3 seconds decide if the viewer keeps watching, not the payoff, not the production quality, the raw immediate reaction to this line)
- Open with a specific, jarring claim, an uncomfortable accusation, or a detail that sounds impossible but is true — never a calm explanation of a concept or topic
- Do NOT start by naming or defining the concept/topic ("X is a tactic where...", "Your brain is wired to...", "X happens when..."). That reads as a lecture intro, not a hook. Lead with the effect on the viewer or the moment itself — explain the mechanism later, once they're already hooked
- No greeting, no "in this video", no channel/topic announcement
- You MUST use this hook instruction, do NOT improvise a different opening: {hook_instruction}
- End the opening sentence on an unresolved question, or a statement that demands to know what happens next
- ABSOLUTELY FORBIDDEN opening phrases (instant disqualification): "What if I told you", "What if I said", "Let me tell you", "Did you know", "Brace yourself", "Buckle up", "Here is the thing", "You won't believe"

OPEN LOOP
- Plant one specific question or unresolved stake in the first two sentences
- Do NOT answer it until the final 20% of the script
- Reference it again once or twice through the middle without resolving it
- When you finally resolve it near the end, recontextualize the hook in the last line — the ending should reframe how the opening line lands

PACING (this script is read aloud by TTS — every rule below is about how it sounds spoken, not how it reads on a page)
- Average sentence 8-14 words. Vary rhythm — never two sentences in a row with the same length or the same emotional temperature
- HARD CAP: no single sentence may exceed 20 words, no exceptions — this applies just as much to the final/payoff line as to every other sentence. A long sentence is not more dramatic, it is harder to follow and harder to read aloud
- One idea per sentence. The moment a sentence needs a second comma to hold a second clause, it should almost always be split into two separate sentences instead — never chain three or more clauses together with commas ("X, and Y, which means Z, so W" is forbidden even without em dashes or semicolons)
- Hitting the target word count matters just as much as sentence length. Never cut the script short to keep sentences short — if more content is needed to reach the word count, add MORE short sentences (another beat, another detail, another escalation), never make existing sentences longer
- The final line (the payoff/reframe) must be SHORT — one clean, short, declarative sentence, not a long recap that restates everything that came before. A short ending lands harder and is easier to follow than a summary
- Escalate roughly every 1-2 sentences with a shift in intensity: a new detail, a reversal, a stake raised. Don't let the tension go flat for more than two sentences. This should feel like a story with rising stakes, not an explainer with facts bolted on
- Name at most ONE technical term or piece of jargon in the entire script. If you introduce a concept, use plain language for it everywhere else — never stack two named concepts back to back, that turns a story into a lecture
- Second person ("you") beats third person ("people") wherever it's natural — a specific, personal, uncomfortable framing beats a general clinical one
- Concrete nouns and numbers over abstractions — never "a lot", say how many; never "a long time", say how long
- Cut any sentence that only sets up another sentence — get straight to the content
- Do not summarize what you're about to say, just say it
- No em dashes, no parentheses, no semicolons — plain spoken punctuation only (periods, commas, question marks)
- Include one unexpected twist or reversal that reframes everything
- If you name or define a term/acronym, explain it in one natural flowing sentence — never spell it out as a bare comma-separated list of words
- Do NOT use hashtags, emojis, or any formatting
- Each script must feel unique — avoid formulaic structure

OUTPUT
Write ONLY the narration itself as plain flowing text — no title, no labels, no timecodes, no visual directions, nothing but the words to be spoken, nothing else:"""

    log.info("Generating %s story (topic=%s)...", style, topic or "random")

    # Scene extraction and motion prompts still use whatever provider is
    # globally configured, since those already degrade gracefully on
    # failure — only story generation needs an explicit override here.
    story_config = dataclasses.replace(
        config, llm_provider=llm_provider, llm_key="", llm_model=llm_model
    )

    best_story = ""
    best_word_count = 0
    for attempt in range(1, 4):
        story = _break_long_sentences(_filter_banned(_call_llm(prompt, story_config)))
        word_count = len(story.split())

        if word_count > best_word_count:
            best_story, best_word_count = story, word_count

        if word_count >= min_acceptable_words:
            log.info("Story generated: %d words", word_count)
            return story

        log.warning(
            "Story attempt %d/3 too short (%d words, likely truncated) — retrying",
            attempt, word_count,
        )

    log.warning(
        "All story attempts came back short — using longest one (%d words)",
        best_word_count,
    )
    return best_story


def generate_title_suggestions(
    style: str = "mind_blowing",
    config: Optional[Config] = None,
) -> list[str]:
    """Suggest 3 viral video title/topic ideas for a given content style.

    Args:
        style: Content style key (see ``STYLES``).
        config: Configuration instance. Uses env vars if not provided.

    Returns:
        A list of 3 short title strings.

    Raises:
        RuntimeError: If the LLM call fails or returns unusable output.
        ValueError: If the style is unknown.
    """
    config = config or get_config()

    if style not in STYLES:
        available = ", ".join(sorted(STYLES.keys()))
        raise ValueError(f"Unknown style '{style}'. Available: {available}")

    style_prompt = STYLES[style]

    prompt = f"""You are a viral short-form video strategist (TikTok/YouTube Shorts).

CHANNEL NICHE: {style_prompt}

Suggest 3 distinct video title/topic ideas for this niche that would hook viewers in the first second.

Rules for each title:
- Short, punchy, 5-12 words
- A specific, surprising, or unsettling claim — never a vague topic label ("Interesting Space Facts")
- No clickbait phrases like "You won't believe", "What if I told you", "Did you know"
- No hashtags, no emojis, no quotation marks
- Each of the 3 must cover a genuinely different fact or angle, not variations of the same one

Return ONLY a JSON array of 3 strings, nothing else:
["title one", "title two", "title three"]"""

    title_config = dataclasses.replace(
        config,
        llm_provider=config.script_llm_provider,
        llm_key="",
        llm_model=config.script_llm_model,
    )

    # 1024, not 300: Replicate-hosted Claude rejects max_tokens below 1024
    # outright, and title_config may now route there (see _call_llm docstring).
    text = _call_llm(prompt, title_config, max_tokens=1024, temperature=1.0)
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        titles = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Title suggestions: LLM returned invalid JSON: {text[:200]}") from exc

    if not isinstance(titles, list) or not titles:
        raise RuntimeError("Title suggestions: LLM returned an empty or non-list response")

    titles = [str(t).strip().strip('"') for t in titles if str(t).strip()]
    if not titles:
        raise RuntimeError("Title suggestions: no usable titles in LLM response")

    return titles[:3]


def list_styles() -> dict[str, str]:
    """Return all available content styles with descriptions."""
    return dict(STYLES)
