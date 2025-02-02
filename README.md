# LangChain Chatbot Sample

A sample project demonstrating how to create an intelligent chatbot using LangChain and LangGraph. This project serves as a reference implementation for building conversational AI applications with modern language models.

## Features

- 🤖 Built with LangChain and LangGraph
- 🧠 Stateful conversation management
- 🔄 Extensible architecture
- ⚡ Modern Python practices
- 📝 Comprehensive documentation
- 🧪 Full test coverage

## Prerequisites

- Python 3.9+
- Poetry (required)
- Just command runner

## Installation

```bash
# Install Just if you haven't already (macOS)
brew install just

# Or on Ubuntu/Debian
# curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin

# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Clone the repository
git clone https://github.com/yourusername/langchain-chatbot-sample.git
cd langchain-chatbot-sample

# Install dependencies (including development dependencies)
just install-dev

# Or install only production dependencies
just install
```

## Development

```bash
# List all available commands
just

# Run tests
just test

# Run linting
just lint

# Format code
just format

# Clean up temporary files
just clean

# Update dependencies
just update

# Show outdated packages
just outdated

# Activate virtual environment
just venv
```

## Usage

```python
from chatbot import ChatBot

bot = ChatBot()
response = bot.chat("Hello, how are you?")
print(response)
```

## Project Structure

```
/
├── config/                  # Configuration files
├── chatbot/                # Main application logic
├── tests/                  # Unit tests
└── ...
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
