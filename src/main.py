from fastapi import FastAPI

app = FastAPI(
    title="Purple Cow Service",
    description="Purple Cow Service Items",
    version="0.0.1"
)

items = [{"id": 0, "name": "bike"}]

@app.get("/", summary="Checks if API is running", description="returns a message to make sure service is up and running")
def read_root():
    return {"Purple Cow Service": "Running"}

# get 
@app.get("/items", summary="Checks if API is running", description="returns a message to make sure service is up and running")
def read_root():
    return items


# set/post
@app.post(
    "/items", summary="Write a file to a s3 bucket",
    description="Write a file to a s3 bucket"
)
def create_item():
    pass

# delete 
@app.delete('/items/{item_id}', summary="Write a file to a s3 bucket",
    description="Write a file to a s3 bucket"
)
def delete_item(item_id: int):
    items.pop(id)