from fastapi import HTTPException
import sys
sys.path.append('..')
from model.models import Item

def delete_item_test(item_id: str):
    result = Item.delete(item_id)
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    