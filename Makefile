.PHONY: setup clean test lint type-check format check-all
# Variables
PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
help:
	@echo "Available commands:"
	@echo "make setup		- Create virtual environment, install dependencies with uv, and install pre-commit hooks"
	@echo "make clean		- Remove virtual environment and cache files"
	@echo "make check		- Run pre-commit checks"
setup: clean
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync
	uv run pre-commit install
clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf **/__pycache__
	rm -rf *.egg-info
	uv run pre-commit uninstall || true
check:
	uv run pre-commit run --all-files
gpush: check
	git add -A && git commit -m "wip $$(date +%F)" && git push
