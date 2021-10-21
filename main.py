from fastapi import FastAPI, Query, Path, Body, UploadFile, File
import uvicorn
import shutil
from typing import List, Optional


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}


@app.post("/upload_img")
async def upload_img(img: List[UploadFile] = File(...)):
    for file in img:
        with open(file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("app", log_level="info")
