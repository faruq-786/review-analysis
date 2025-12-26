import sys
from litellm import completion
from app.llm.llm_config import get_active_llm
from app.logs import get_logger
from app.exceptions import CustomException

logger = get_logger(__name__)

def analyze_restaurant(reviews, question):
    try:
        logger.info("Starting restaurant analysis via LLM")

        reviews_text = "\n".join(
            f"- {r['food_item']} | Rating: {r['rating']} | {r['review']}"
            for r in reviews
        )

        prompt = f"""
You are a friendly, sharp restaurant performance assistant speaking directly to the restaurant owner.

Rules:
- Conversational
- Short and insightful
- No markdown
- No tables

Customer reviews:
{reviews_text}

Owner question:
"{question}"

Answer naturally.
"""

        llm = get_active_llm()

        logger.info(
            f"Calling LLM model={llm['model']} "
            f"temperature={llm['temperature']} "
            f"max_tokens={llm['max_tokens']}"
        )

        response = completion(
            model=llm["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=llm["temperature"],
            max_tokens=llm["max_tokens"],
        )

        logger.info("LLM response received successfully")

        return response.choices[0].message.content

    except Exception as e:
        logger.error("Error while generating LLM response", exc_info=True)
        raise CustomException(e, sys)
