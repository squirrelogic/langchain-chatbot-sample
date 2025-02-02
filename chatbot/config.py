"""Configuration management for the chatbot."""

import os
import getpass
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv


def _set_env(var: str) -> None:
    """Set environment variable if not already set, prompting user for input."""
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


def setup_environment() -> None:
    """Set up the environment variables needed for the chatbot."""
    # Try to load from .env file first
    env_path = Path(".env")
    if env_path.exists():
        load_dotenv(env_path)

    # Ensure required environment variables are set
    _set_env("OPENAI_API_KEY")


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file and override with environment variables."""
    # Load base config from YAML
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Override with environment variables if they exist
    if model := os.getenv("OPENAI_MODEL"):
        config["llm"]["model"] = model

    if temperature := os.getenv("OPENAI_TEMPERATURE"):
        config["llm"]["temperature"] = float(temperature)

    if max_tokens := os.getenv("OPENAI_MAX_TOKENS"):
        config["llm"]["max_tokens"] = int(max_tokens)

    if log_level := os.getenv("LOG_LEVEL"):
        config["logging"]["level"] = log_level

    return config


def get_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """Get configuration after ensuring environment is set up."""
    setup_environment()
    return load_config(config_path)
