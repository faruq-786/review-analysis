from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.mongodb.reviews_repo import fetch_all_reviews
from app.llm.llm_client import analyze_restaurant
from app.sqlite.chat_repo import save_chat, fetch_chat_history

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    reviews = fetch_all_reviews(request.restaurant_name)

    if not reviews:
        return {"answer": "No reviews found for this restaurant."}

    answer = analyze_restaurant(reviews, request.question)

    save_chat(
        request.restaurant_name,
        request.question,
        answer
    )

    return {"answer": answer}

@router.get("/chat/history")
def chat_history(restaurant_name: str):
    history = fetch_chat_history(restaurant_name)
    return history
