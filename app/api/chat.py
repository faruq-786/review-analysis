from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest
from app.mongodb.reviews import fetch_all_reviews
from app.llm.llm_client import analyze_restaurant
from app.sqlite.chat_repo import save_chat, fetch_chat_history
from app.logs import get_logger
from app.exceptions import CustomException

router = APIRouter()
logger = get_logger(__name__)

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        logger.info(
            f"Chat request received | restaurant={request.restaurant_name}"
        )

        reviews = fetch_all_reviews(request.restaurant_name)

        if not reviews:
            logger.info("No reviews found for restaurant")
            return {"answer": "No reviews found for this restaurant."}

        answer = analyze_restaurant(reviews, request.question)

        save_chat(
            request.restaurant_name,
            request.question,
            answer
        )

        logger.info("Chat request processed successfully")
        return {"answer": answer}

    except CustomException as ce:
        logger.error(str(ce))
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/chat/history")
def chat_history(restaurant_name: str):
    try:
        logger.info(f"Fetching chat history | restaurant={restaurant_name}")
        return fetch_chat_history(restaurant_name)

    except CustomException as ce:
        logger.error(str(ce))
        raise HTTPException(status_code=500, detail="Internal server error")
