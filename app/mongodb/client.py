import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv
from app.logs import get_logger
from app.exceptions import CustomException

load_dotenv()
logger = get_logger(__name__)

MONGO_URI = os.getenv("MONGO_URI")

try:
    logger.info("Initializing MongoDB client")
    client = MongoClient(MONGO_URI)
    logger.info("MongoDB client initialized successfully")

except Exception as e:
    logger.error("Failed to initialize MongoDB client", exc_info=True)
    raise CustomException(e, sys)
