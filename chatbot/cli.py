"""Command-line interface for the chatbot."""

import asyncio
import uuid
from typing import Any, Dict, List

from aioconsole import ainput

from .config import get_config
from .graph import build_runnable_graph


async def main() -> None:
    """Run the chatbot in interactive mode."""
    # Load configuration (this will also set up the environment)
    system_config = get_config()

    # Build the graph
    chain = await build_runnable_graph(system_config)

    # Initialize state
    state: Dict[str, List[Any]] = {"messages": []}

    print("Chatbot initialized. Type 'quit' or 'exit' to end the conversation.")
    print("You can try commands like:")
    print("- What's 123 * 456?")
    print("- What's the weather in London?")
    print("-" * 50)

    # Generate a unique thread ID for this conversation
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    while True:
        try:
            # Get user input asynchronously
            user_input = await ainput("\nYou: ")
            user_input = user_input.strip()

            # Check for exit command
            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye!")
                break

            # Add user message to state
            state["messages"].append({"role": "user", "content": user_input})

            # Get bot response
            new_state = await chain.ainvoke(state, config)
            response = new_state["messages"][-1]

            # Update state
            state = new_state

            print(f"\nBot: {response.content}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            break


def run() -> None:
    """Entry point for the CLI."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    run()
