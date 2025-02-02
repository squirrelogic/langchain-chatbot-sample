"""Common test fixtures for the chatbot package."""

import pytest
from typing import Dict, Any
import yaml
from pathlib import Path


@pytest.fixture
def test_config() -> Dict[str, Any]:
    """Load test configuration."""
    return {
        "app": {"name": "Test Chatbot", "version": "0.1.0", "environment": "test"},
        "llm": {
            "provider": "openai",
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_tokens": 150,
        },
        "memory": {"type": "conversation_buffer", "max_turns": 5, "k_context": 3},
    }


@pytest.fixture
def mock_response() -> str:
    """Return a mock chatbot response."""
    return "This is a test response from the chatbot."
