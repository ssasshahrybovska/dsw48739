from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Note(BaseModel):
    id: int
    title: str
    content: str


notes = []


@app.get("/")
def read_root():
    return {"message": "Sasha API is running!"}
