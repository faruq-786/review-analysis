from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.sqlite.database import Base, engine, SessionLocal

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def save_chat(restaurant_name, question, answer):
    db = SessionLocal()
    chat = ChatHistory(
        restaurant_name=restaurant_name,
        question=question,
        answer=answer
    )
    db.add(chat)
    db.commit()
    db.close()

def fetch_chat_history(restaurant_name):
    db = SessionLocal()
    data = db.query(ChatHistory).filter(
        ChatHistory.restaurant_name == restaurant_name
    ).all()
    db.close()
    return data
