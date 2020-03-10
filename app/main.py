from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/query/")
async def query_parameter(skip: int):
    return {"skip": skip}


@app.post("/request/")
async def create_item(item: Item):
    return item


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
