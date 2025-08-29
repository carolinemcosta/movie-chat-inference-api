from enum import Enum


class GroqModels(Enum):
    """List of Groq models available."""

    LLAMA_3_3_70b: str = "llama-3.3-70b-versatile"
    LLAMA_4_SCOUT: str = "meta-llama/llama-4-scout-17b-16e-instruct"
    GPT_OSS_20b: str = "openai/gpt-oss-20b"
    GPT_OSS_120b: str = "openai/gpt-oss-120b"


class GroqParameters(Enum):
    """List of Groq parameters."""

    TEMPERATURE: int = 0
    TIMEOUT: int = 30
    STREAMING: bool = False
    MAX_TOKENS: int = 500
