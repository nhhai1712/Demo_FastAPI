import sys
sys.path.append('..')
from model.models import Item

def read_items_test():
    items = []
    for item in Item.get_all():
        items.append({
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item["description"]
        })
    return items