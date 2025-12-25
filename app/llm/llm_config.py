from app.config import load_llm_config

def get_active_llm():
    config = load_llm_config()

    llm_cfg = config["llm"]
    providers = config["providers"]

    active_provider = llm_cfg["active_provider"]
    active_model = llm_cfg["active_model"]

    if active_provider not in providers:
        raise ValueError(
            f"Provider '{active_provider}' not defined in llm.yaml"
        )

    expected_prefix = providers[active_provider]["prefix"]

    if not active_model.startswith(expected_prefix):
        raise ValueError(
            f"Model '{active_model}' does not match provider '{active_provider}' "
            f"(expected prefix '{expected_prefix}')"
        )

    return {
        "provider": active_provider,
        "model": active_model
    }
