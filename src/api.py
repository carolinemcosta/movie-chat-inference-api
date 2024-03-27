from fastapi import FastAPI

from src.routers import movie

app = FastAPI()


app.include_router(movie.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
