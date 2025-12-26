import sys
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.sqlite.database import Base, engine, SessionLocal
from app.logs import get_logger
from app.exceptions import CustomException

logger = get_logger(__name__)

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def save_chat(restaurant_name, question, answer):
    try:
        logger.info("Saving chat history")

        db = SessionLocal()
        chat = ChatHistory(
            restaurant_name=restaurant_name,
            question=question,
            answer=answer
        )
        db.add(chat)
        db.commit()
        db.close()

        logger.info("Chat history saved successfully")

    except Exception as e:
        logger.error("Failed to save chat history", exc_info=True)
        raise CustomException(e, sys)

def fetch_chat_history(restaurant_name):
    try:
        logger.info(f"Fetching chat history | restaurant={restaurant_name}")

        db = SessionLocal()
        data = db.query(ChatHistory).filter(
            ChatHistory.restaurant_name == restaurant_name
        ).all()
        db.close()

        logger.info(f"Fetched {len(data)} chat records")
        return data

    except Exception as e:
        logger.error("Failed to fetch chat history", exc_info=True)
        raise CustomException(e, sys)
