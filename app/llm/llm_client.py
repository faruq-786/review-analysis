import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY,
    temperature=0.3
)

def analyze_restaurant(reviews, question):
    reviews_text = "\n".join(
        f"- {r['food_item']} | Rating: {r['rating']} | {r['review']}"
        for r in reviews
    )

    prompt = f"""
You are a restaurant analytics assistant.

Customer Reviews:
{reviews_text}

Client Question:
{question}

Give a clear, business-friendly answer.
"""

    response = llm.invoke(prompt)

    # LangChain returns an AIMessage
    return response.content
