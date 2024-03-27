from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def ask_movie(question: str):
    """_summary_"""

    chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
    system = "You are a helpful movie recommendation assistant. \
        You recommend movies based on the human's taste and mood"
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    response = chain.invoke({"text": question})
    return response
