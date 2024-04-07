from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from src.models.chat import ModelResponse, UserRequest
from src.models.enums import GroqParameters
from src.utils.metadata import build_metadata

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def recommend(body: UserRequest):
    """Recommend a movie using the Groq API based on the user input."""
    chat = ChatGroq(
        temperature=GroqParameters.TEMPERATURE.value,
        request_timeout=GroqParameters.TIMEOUT.value,
        streaming=GroqParameters.STREAMING.value,
        max_tokens=GroqParameters.MAX_TOKENS.value,
        model_name=body.model.value,
    )
    system = "You are a helpful movie recommendation assistant. \
        You recommend movies based on the human's taste and mood"
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    response = chain.invoke({"text": {body.question}})

    return ModelResponse(
        answer=response.content, metadata=build_metadata(response.response_metadata)
    )
