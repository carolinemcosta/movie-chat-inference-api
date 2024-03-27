from fastapi import FastAPI

from src.routers import chat, movie

app = FastAPI()


app.include_router(movie.router)
app.include_router(chat.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
