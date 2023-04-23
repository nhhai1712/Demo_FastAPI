from fastapi import FastAPI, HTTPException
import uvicorn
import sys
sys.path.append('..')
from model.models import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items():
    items = []
    for item in Item.get_all():
        items.append({
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item["description"]
        })
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = Item.get_by_id(item_id)
    data = []
    data.append({
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item["description"]
    })
    if item:
        return data
    else:
        raise HTTPException(status_code=404, detail="Item not found")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)