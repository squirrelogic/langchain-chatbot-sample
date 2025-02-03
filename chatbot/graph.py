"""Graph implementation for the chatbot using LangGraph."""

from typing import Annotated, Any, Dict
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from .bot import chatbot, create_llm
from .tools import default_tools


class State(TypedDict):
    """State definition for the chatbot graph."""

    messages: Annotated[list, add_messages]


def create_graph(config: Dict[str, Any]) -> StateGraph:
    """Create a new StateGraph for the chatbot.

    Args:
        config: Configuration dictionary containing LLM settings.

    Returns:
        A configured StateGraph instance.
    """
    # Initialize the graph with our State type
    graph = StateGraph(State)

    # Create the LLM instance with bound tools
    llm = create_llm(config)

    # Define how to process the response
    def process_response(state: State) -> dict:
        """Process the state and generate a response."""
        return chatbot(state, llm)

    # Add nodes to the graph
    graph.add_node("chatbot", process_response)
    tool_node = ToolNode(tools=default_tools)
    graph.add_node("tools", tool_node)

    graph.add_conditional_edges(
        "chatbot",
        tools_condition,
    )
    # Any time a tool is called, we return to the chatbot to decide the next step
    graph.add_edge("tools", "chatbot")
    graph.set_entry_point("chatbot")

    return graph


async def build_runnable_graph(config: Dict[str, Any]) -> Any:
    """Build and compile the graph into a runnable chain.

    Args:
        config: Configuration dictionary containing LLM settings.

    Returns:
        A compiled graph that can be invoked.
    """
    graph = create_graph(config)
    return graph.compile()
