"""backend/config.py — API key + Anthropic client factory

.env BUG FIX:
  load_dotenv() without a path only works if the process is launched
  from the same directory as .env.
  We now resolve the .env path relative to THIS file, so it always works
  whether you run `python main.py` or `uvicorn main:app` from anywhere.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Always find .env relative to the project root (one level above backend/)
_ROOT = Path(__file__).resolve().parent.parent
_ENV  = _ROOT / ".env"
load_dotenv(dotenv_path=_ENV, override=False)


def get_anthropic_key() -> str:
    return os.getenv("ANTHROPIC_API_KEY", "")


def make_client(api_key: str = ""):
    from anthropic import Anthropic
    key = api_key.strip() if api_key else ""
    if not key:
        key = get_anthropic_key().strip()
    if not key or key == "sk-ant-your-api-key-here":
        raise ValueError(
            "No valid Anthropic API key found. "
            "Set ANTHROPIC_API_KEY in .env or pass it in the request."
        )
    return Anthropic(api_key=key)


def extract_text(resp) -> str:
    """Join the text blocks of a Claude Messages API response into one string."""
    return "".join(block.text for block in resp.content if block.type == "text")


# Model assignments per agent — cost + quality balanced
MODELS = {
    "router":      "claude-haiku-4-5",  # Fast intent detection
    "scorer":      "claude-opus-5",     # Precise ATS evaluation
    "optimizer":   "claude-opus-5",     # Resume optimization
    "builder":     "claude-opus-5",     # Interactive fresher builder
    "advisor":     "claude-opus-5",     # Score advisor
    "reframer":    "claude-opus-5",     # Role reframing
    "interviewer": "claude-haiku-4-5",  # Interview prep / general chat
    "chat":        "claude-haiku-4-5",  # General conversation
}
