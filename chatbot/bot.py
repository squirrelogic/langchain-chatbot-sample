"""Main chatbot implementation."""

from typing import Any, Dict, List

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage

from .tools import default_tools


def create_llm(config: Dict[str, Any]) -> ChatOpenAI:
    """Create and configure the LLM with tools.

    Args:
        config: Configuration dictionary containing LLM settings.

    Returns:
        Configured ChatOpenAI instance with bound tools.
    """
    # Initialize the base LLM
    llm = ChatOpenAI(
        model=config["llm"]["model"], temperature=config["llm"]["temperature"]
    )

    # Bind tools to the LLM
    return llm.bind_tools(default_tools)


def chatbot(state: Dict[str, List[Any]], llm: ChatOpenAI) -> Dict[str, List[Any]]:
    """Process the current state and generate a response.

    Args:
        state: Current conversation state with messages.
        llm: The language model to use for responses.

    Returns:
        Updated state with new message.
    """
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
