from enum import Enum


class GroqModels(Enum):
    """List of Groq models available."""

    MIXTRAL_8X7B_32768: str = "mixtral-8x7b-32768"
    LLAMA2_70B_4096: str = "llama2-70b-4096"
    GEMMA_7B_IT: str = "gemma-7b-it"


class GroqParameters(Enum):
    """List of Groq parameters."""

    TEMPERATURE: int = 0
    TIMEOUT: int = 30
    STREAMING: bool = False
    MAX_TOKENS: int = 500
