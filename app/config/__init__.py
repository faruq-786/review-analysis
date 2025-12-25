import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_llm_config():
    config_path = BASE_DIR / "config" / "llm.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
