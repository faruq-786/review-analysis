import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from app.logs import get_logger
from app.exceptions import CustomException

load_dotenv()
logger = get_logger(__name__)

SQLITE_DB = os.getenv("SQLITE_DB")

try:
    logger.info("Initializing SQLite database")
    engine = create_engine(f"sqlite:///{SQLITE_DB}")
    SessionLocal = sessionmaker(bind=engine)
    Base = declarative_base()
    logger.info("SQLite database initialized successfully")

except Exception as e:
    logger.error("Failed to initialize SQLite database", exc_info=True)
    raise CustomException(e, sys)
