import sys
sys.path.append('..')
from model.models import Item

def create_item_test(name: str, description: str):
    item = Item(name, description)
    result = item.save()
    data = []
    data.append({
        "id": str(result.inserted_id),
        "name": name,
        "description": description
    })
    return data 
