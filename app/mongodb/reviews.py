import os
import sys
from app.mongodb.client import client
from dotenv import load_dotenv
from app.logs import get_logger
from app.exceptions import CustomException

load_dotenv()
logger = get_logger(__name__)

MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

def fetch_all_reviews(restaurant_name: str):
    try:
        logger.info(f"Fetching reviews | restaurant={restaurant_name}")

        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]

        reviews = list(
            collection.find(
                {"restaurant_name": restaurant_name},
                {"_id": 0}
            )
        )

        logger.info(f"Fetched {len(reviews)} reviews")
        return reviews

    except Exception as e:
        logger.error("Error fetching reviews from MongoDB", exc_info=True)
        raise CustomException(e, sys)
