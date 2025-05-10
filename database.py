import os
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class BaseModelService:
    database_client: MongoClient
    collection_name: str

    def __init__(self, collection_name: str):
        MONGO_URL = os.getenv("MONGO_URL")
        MONGO_DB = os.getenv("MONGO_DB")

        client = MongoClient(MONGO_URL)

        db_client = client[MONGO_DB]

        self.database = db_client
        self.collection_name = collection_name

    def find_all(self, query = {}):
        query["enabled"] = True
        return self.database[self.collection_name].find(query).to_list()
    
    def insert(self, props):
        props["enabled"] = True
        props["created_at"] = datetime.datetime.now()
        props["updated_at"] = datetime.datetime.now()

        return self.database[self.collection_name].insert_one(props)
    