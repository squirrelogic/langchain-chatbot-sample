# List available commands
default:
    @just --list

# Install only production dependencies
install:
    poetry install --no-dev

# Install all dependencies including development ones
install-dev:
    poetry install

# Run tests with coverage
test:
    poetry run pytest tests/ -v --cov=chatbot

# Run all linting checks
lint: format-check ruff-check mypy-check

# Format code and apply fixes
format:
    poetry run black .
    poetry run ruff --fix .

# Check formatting without making changes
format-check:
    poetry run black --check .

# Run ruff linter checks
ruff-check:
    poetry run ruff check .

# Run mypy type checking
mypy-check:
    poetry run mypy chatbot/

# Clean up temporary files and caches
clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete
    find . -type f -name "*.pyd" -delete
    find . -type f -name ".coverage" -delete
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type d -name "*.egg" -exec rm -rf {} +
    find . -type d -name ".pytest_cache" -exec rm -rf {} +
    find . -type d -name ".mypy_cache" -exec rm -rf {} +
    find . -type d -name ".ruff_cache" -exec rm -rf {} +
    find . -type d -name "dist" -exec rm -rf {} +
    find . -type d -name "build" -exec rm -rf {} +

# Update all dependencies to their latest versions
update:
    poetry update

# Show outdated packages
outdated:
    poetry show --outdated

# Create and activate a new virtual environment
venv:
    poetry shell
