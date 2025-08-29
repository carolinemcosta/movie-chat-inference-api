from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

from .enums import GroqModels


class UserRequest(BaseModel):
    """UserQuestion model."""

    question: str
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

    answer: str
    metadata: ResponseMetadata
