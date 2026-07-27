"""
Configuration management for clipforge.

Reads settings from environment variables with sensible defaults.
All config is centralized here — no hardcoded values anywhere else.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


# ── Default models per provider ──────────────────────────────────────────────

DEFAULT_MODELS: dict[str, str] = {
    "groq": "llama-3.3-70b-versatile",
    "openai": "gpt-4o-mini",
    "anthropic": "claude-haiku-4-5-20251001",
    "replicate": "openai/gpt-oss-120b",
}

# ── API endpoints ────────────────────────────────────────────────────────────

API_ENDPOINTS: dict[str, str] = {
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "openai": "https://api.openai.com/v1/chat/completions",
    "anthropic": "https://api.anthropic.com/v1/messages",
}

# Standard provider env vars used as a fallback when CLIPFORGE_LLM_KEY isn't set.
PROVIDER_KEY_ENV: dict[str, str] = {
    "groq": "GROQ_API_KEY",
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
}

# ── Available TTS voices ─────────────────────────────────────────────────────

VOICES: dict[str, str] = {
    "andrew": "en-US-AndrewMultilingualNeural",
    "brian": "en-US-BrianMultilingualNeural",
    "ava": "en-US-AvaMultilingualNeural",
    "emma": "en-US-EmmaMultilingualNeural",
    "ryan": "en-GB-RyanNeural",
    "sonia": "en-GB-SoniaNeural",
    "libby": "en-GB-LibbyNeural",
    "guy": "en-US-GuyNeural",
    "jenny": "en-US-JennyNeural",
    "aria": "en-US-AriaNeural",
    "davis": "en-US-DavisNeural",
    "jane": "en-US-JaneNeural",
    "jason": "en-US-JasonNeural",
    "tony": "en-US-TonyNeural",
    "nancy": "en-US-NancyNeural",
    "sara": "en-US-SaraNeural",
}


@dataclass
class Config:
    """Central configuration for clipforge.

    All values can be overridden via environment variables prefixed
    with ``CLIPFORGE_`` or passed directly to functions.
    """

    llm_provider: str = field(
        default_factory=lambda: os.environ.get("CLIPFORGE_LLM_PROVIDER", "groq")
    )
    llm_key: str = field(
        default_factory=lambda: os.environ.get("CLIPFORGE_LLM_KEY", "")
    )
    llm_model: Optional[str] = field(
        default_factory=lambda: os.environ.get("CLIPFORGE_LLM_MODEL")
    )
    replicate_key: str = field(
        default_factory=lambda: os.environ.get("CLIPFORGE_REPLICATE_KEY", "")
    )
    voice: str = field(
        default_factory=lambda: os.environ.get(
            "CLIPFORGE_VOICE", "en-US-AndrewMultilingualNeural"
        )
    )
    output_dir: Path = field(
        default_factory=lambda: Path(
            os.environ.get("CLIPFORGE_OUTPUT_DIR", "./output")
        )
    )

    def __post_init__(self) -> None:
        if not self.replicate_key:
            self.replicate_key = os.environ.get("REPLICATE_API_TOKEN", "")
        if not self.llm_key:
            if self.llm_provider == "replicate":
                self.llm_key = self.replicate_key
            else:
                env_var = PROVIDER_KEY_ENV.get(self.llm_provider)
                if env_var:
                    self.llm_key = os.environ.get(env_var, "")

    @property
    def resolved_model(self) -> str:
        """Return the LLM model name, falling back to provider default."""
        if self.llm_model:
            return self.llm_model
        return DEFAULT_MODELS.get(self.llm_provider, DEFAULT_MODELS["groq"])

    @property
    def llm_endpoint(self) -> str:
        """Return the API endpoint URL for the configured provider."""
        return API_ENDPOINTS.get(self.llm_provider, API_ENDPOINTS["groq"])

    @property
    def has_replicate(self) -> bool:
        """Check if Replicate image generation is available."""
        return bool(self.replicate_key)

    @property
    def has_llm(self) -> bool:
        """Check if an LLM API key is configured."""
        return bool(self.llm_key)

    def ensure_output_dir(self) -> Path:
        """Create and return the output directory."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        return self.output_dir

    def summary(self) -> dict[str, str]:
        """Return a human-readable config summary (keys masked)."""
        return {
            "LLM Provider": self.llm_provider,
            "LLM Model": self.resolved_model,
            "LLM Key": _mask(self.llm_key),
            "Replicate Token": _mask(self.replicate_key),
            "Voice": self.voice,
            "Output Dir": str(self.output_dir),
        }


def _mask(key: str) -> str:
    """Mask an API key for safe display."""
    if not key:
        return "(not set)"
    if len(key) <= 8:
        return "****"
    return f"{key[:4]}...{key[-4:]}"


def get_config() -> Config:
    """Create a Config instance from current environment."""
    return Config()
