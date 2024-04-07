from fastapi import FastAPI

from src.routers import chat

app = FastAPI()


app.include_router(chat.router)


@app.get("/")
async def root():
    return {
        "message": "Hello, I am MoReChat! I'm a chatbot for movie recommendations. \n\What do you feel like watching?"
    }
