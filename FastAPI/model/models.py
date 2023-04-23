# connect fastapi with mongodb
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
mongo_host = os.environ.get('mongodb_host')
mongo_port = int(os.environ.get('mongodb_port'))
mongo_db = os.environ.get('mongodb_db')
mongo_collection = os.environ.get('mongodb_collection')

mongo_uri = f'mongodb://{mongo_host}:{mongo_port}/'
client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def save(self):
        return collection.insert_one({
            "name": self.name,
            "description": self.description
        })

    @staticmethod
    def get_all():
        return collection.find()

    @staticmethod
    def get_by_id(id: str):
        return collection.find_one({"_id": ObjectId(id)})

    @staticmethod
    def update(id: str, name: str, description: str):
        return collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "description": description}})

    @staticmethod
    def delete(id: str):
        return collection.delete_one({"_id": ObjectId(id)})
