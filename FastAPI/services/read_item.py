import sys
sys.path.append('..')
from fastapi import HTTPException
from model.models import Item

def read_item_test(item_id: str):
    item = Item.get_by_id(item_id)
    if item:
        return {
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item["description"]
        }
    else:
        raise HTTPException(status_code=404, detail="Item not found")