from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

from .enums import GroqModels


class UserRequest(BaseModel):
    """UserQuestion model."""

    question: Annotated[
        str, StringConstraints(max_length=200, strict=True, pattern="[^0-9a-zA-Z:,]+")
    ]
    model: GroqModels


class ResponseMetadata(BaseModel):
    """Model response metadata."""

    model_name: str
    completion_time: float
    prompt_time: float
    prompt_tokens: int
    total_tokens: int


class ModelResponse(BaseModel):
    """ModelAnswer model."""

    answer: Annotated[str, StringConstraints(strict=True, pattern="[^0-9a-zA-Z:,]+")]
    metadata: ResponseMetadata
