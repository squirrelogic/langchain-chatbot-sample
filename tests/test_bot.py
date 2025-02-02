"""Test cases for the chatbot core functionality."""

import pytest
from typing import Dict, Any

# These will be implemented later
from chatbot import ChatBot  # type: ignore


def test_chatbot_initialization(test_config: Dict[str, Any]) -> None:
    """Test that the chatbot can be initialized with config."""
    bot = ChatBot(config=test_config)
    assert bot is not None
    assert bot.config == test_config


def test_chatbot_response(test_config: Dict[str, Any], mock_response: str) -> None:
    """Test that the chatbot can generate responses."""
    bot = ChatBot(config=test_config)
    response = bot.chat("Hello!")
    assert isinstance(response, str)
    assert len(response) > 0


@pytest.mark.asyncio
async def test_chatbot_async_response(
    test_config: Dict[str, Any], mock_response: str
) -> None:
    """Test that the chatbot can generate responses asynchronously."""
    bot = ChatBot(config=test_config)
    response = await bot.achat("Hello!")
    assert isinstance(response, str)
    assert len(response) > 0


def test_chatbot_memory(test_config: Dict[str, Any]) -> None:
    """Test that the chatbot maintains conversation memory."""
    bot = ChatBot(config=test_config)
    first_response = bot.chat("My name is Alice")
    second_response = bot.chat("What's my name?")
    assert "Alice" in second_response.lower()
