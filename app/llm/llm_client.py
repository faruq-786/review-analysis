from litellm import completion
from app.llm.llm_config import get_active_llm
from dotenv import load_dotenv

load_dotenv()

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

    llm = get_active_llm()

    response = completion(
        model=llm["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=llm["temperature"],
        max_tokens=llm["max_tokens"]
    )

    return response.choices[0].message.content
