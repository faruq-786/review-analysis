import sys
from app.config import load_llm_config
from app.logs import get_logger
from app.exceptions import CustomException

logger = get_logger(__name__)

def get_active_llm():
    try:
        logger.info("Loading LLM configuration")

        config = load_llm_config()
        llm_cfg = config["llm"]
        providers = config["providers"]

        active_provider = llm_cfg["active_provider"]
        active_model = llm_cfg["active_model"]

        logger.info(
            f"Active provider: {active_provider}, Active model: {active_model}"
        )

        if active_provider not in providers:
            raise ValueError(f"Provider '{active_provider}' not defined")

        expected_prefix = providers[active_provider]["prefix"]
        if not active_model.startswith(expected_prefix):
            raise ValueError(
                f"Model '{active_model}' does not match provider '{active_provider}'"
            )

        generation_cfg = llm_cfg.get("generation", {})
        temperature = generation_cfg.get("temperature", 0.4)
        max_tokens = generation_cfg.get("max_tokens", 500)

        return {
            "provider": active_provider,
            "model": active_model,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

    except Exception as e:
        logger.error("Failed to load LLM configuration", exc_info=True)
        raise CustomException(e, sys)
