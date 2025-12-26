from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.logs import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Restaurant Performance Chatbot")

logger.info("Starting Restaurant Performance Chatbot API")
app.include_router(chat_router)
