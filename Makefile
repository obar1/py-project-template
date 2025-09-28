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
setup:
	curl -LsSf https://astral.sh/uv/install.sh | sh
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
gpush:
	git add -A && git commit -m "wip $$(date +%F)" && git push
