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
You are a friendly, sharp restaurant performance assistant speaking directly to the restaurant owner.

Your goal:
- Sound natural, confident, and helpful
- Avoid sounding like a report or consultant document
- Do NOT use tables, markdown, headings, or bullet symbols
- Keep the answer short, engaging, and easy to read
- Use simple language and a conversational tone
- Focus on what's going well and what can be improved
- Give at most 2-3 practical suggestions

Context:
These are real customer reviews from the restaurant.

Reviews:
{reviews_text}

The restaurant owner asks:
"{question}"

Respond as if you are talking to them in a real conversation.
"""
    response = llm.invoke(prompt)
    return response.content
