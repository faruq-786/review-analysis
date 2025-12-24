from pydantic import BaseModel

class ChatRequest(BaseModel):
    restaurant_name: str
    question: str
