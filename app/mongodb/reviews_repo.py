import os
from app.mongodb.client import client
from dotenv import load_dotenv
load_dotenv()
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

def fetch_all_reviews(restaurant_name: str):
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    reviews = list(
        collection.find(
            {"restaurant_name": restaurant_name},
            {"_id": 0}
        )
    )
    return reviews
