"""Chatbot package."""

from typing import Any, Dict, Awaitable

from .config import get_config
from .graph import build_runnable_graph

__version__ = "0.1.0"


def create_chatbot() -> Awaitable[Any]:
    """Create a new chatbot instance.

    Returns:
        A coroutine that when awaited returns a runnable chatbot chain.
    """
    config = get_config()
    return build_runnable_graph(config)


__all__ = ["create_chatbot"]
