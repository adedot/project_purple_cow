from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="Purple Cow Service",
    description="Purple Cow Service Items",
    version="0.0.1"
)

items = { 1: {"name": "bike"}}

class Item(BaseModel):
    name: str

@app.get("/", summary="Checks if API is running", description="returns a message to make sure service is up and running")
def read_root():
    return {"Purple Cow Service": "Running"}

# get 
@app.get("/items")
def get_items():
    return items

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
    
# delete 
@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    del items[item_id]