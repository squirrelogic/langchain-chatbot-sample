"""
LangChain Chatbot Sample
A sample project demonstrating how to create an intelligent chatbot using LangChain and LangGraph.
"""

__version__ = "0.1.0"

from typing import Any, Dict, List, Optional

# These will be implemented in separate files
from .bot import ChatBot  # type: ignore
from .config import load_config  # type: ignore

__all__ = ["ChatBot", "load_config"]
