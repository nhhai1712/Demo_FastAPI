from fastapi import FastAPI
from services.read_root import read_root_test
from services.read_items import read_items_test 
from services.read_item import read_item_test
from services.create import create_item_test
from services.update import update_item_test
from services.delete import delete_item_test
app = FastAPI()

@app.get("/")
async def root():
    return read_root_test()

@app.get("/items")
async def read_items():
    return read_items_test()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return read_item_test(item_id)
@app.post("/items/")
async def create_item(name: str, description: str):
    return create_item_test(name, description)

# update da in databases
@app.put("/items/{item_id}")
async def update_item(item_id: str, name: str, description: str):
   return update_item_test(item_id, name, description)

# delete data in databases
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
   return delete_item_test(item_id)
