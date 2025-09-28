.PHONY: setup clean test lint type-check format check-all
# Variables
PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
SRC_DIR := src
TEST_DIR := tests
help:
	@echo "Available commands:"
	@echo "  make setup        - Create virtual environment, install dependencies with uv, and install pre-commit hooks"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo " "
	@echo "  make test         - Run all tests"
	@echo "  make lint         - Run pylint"
	@echo "  make type-check   - Run mypy type checking"
	@echo "  make format       - Format code with black"
	@echo "  make refactor     - Run all checks"
setup:
	uv sync
	uv run pre-commit install
clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf **/__pycache__
test:
	uv run pytest $(TEST_DIR) -v
lint:
	uv run pylint $(SRC_DIR) $(TEST_DIR)
type-check:
	uv run mypy $(SRC_DIR) $(TEST_DIR)
format:
	uv run black $(SRC_DIR) $(TEST_DIR)
	find . -maxdepth 2 -type f -name "*.ipynb" | xargs -I {} bash -c "uv run black '{}'"
refactor: format lint type-check test
gwip:
	git add -A && git commit -m "wip $$(date +%F)" && git push
gpush: refactor gwip
