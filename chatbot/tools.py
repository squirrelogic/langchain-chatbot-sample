"""Tool definitions and tool node implementation."""

import json
from typing import Any, Dict, List

from langchain.tools import BaseTool
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"


@tool
def get_current_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather in a given location."""
    # This is a mock implementation
    return f"The current weather in {location} is 22°{unit[0].upper()}"


# Create default tools list
default_tools = [calculator, get_current_weather]
