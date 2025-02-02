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
- Poetry (recommended) or pip

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/langchain-chatbot-sample.git
cd langchain-chatbot-sample

# Install dependencies
make install
```

## Development Setup

```bash
# Install development dependencies
make install-dev

# Run tests
make test

# Run linting
make lint
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
├── chatbot/                 # Main application logic
├── tests/                   # Unit tests
└── ...
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
