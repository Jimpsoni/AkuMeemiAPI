import fastapi
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Message": "Hello, this is a API to get Donald Duck memes"}


@app.get("/item/{item_id}")
def get_item(item_id: str):
    return fastapi.responses.FileResponse(f"./images/{item_id}.jpg")
