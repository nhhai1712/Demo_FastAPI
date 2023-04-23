from fastapi import HTTPException
import sys
sys.path.append('..')
from model.models import Item

def update_item_test(item_id: str, name: str, description: str):
    result = Item.update(item_id, name, description)
    data = []
    data.append({
        "id": item_id,
        "name": name,
        "description": description
    })
    if result.modified_count == 1:
        return data
    else:
        raise HTTPException(status_code=404, detail="Item not found")
