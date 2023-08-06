from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from common_errors import Error

app = FastAPI()

# In-memory database simulation
db = []
item_id = 1

class Item(BaseModel):
    def __init__(self, name: str, description: str):
        global item_id
        self.id:int = item_id
        self.name:str = name
        self.description:str = description
        item_id += 1

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return db[skip : skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=Error.NOT_FOUND)

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(db):
        if item.id == item_id:
            db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail=Error.NOT_FOUND)

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for idx, item in enumerate(db):
        if item.id == item_id:
            deleted_item = db.pop(idx)
            return deleted_item
    raise HTTPException(status_code=404, detail=Error.NOT_FOUND)
