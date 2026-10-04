.PHONY: install test lint

install:
	cd backend && uv sync
	cd agents && uv sync --extra maf
	cd frontend && npm install

test:
	cd backend && uv run pytest
	cd agents && uv run pytest
	cd frontend && npm run build

lint:
	cd backend && uv run ruff check . && uv run mypy app
	cd agents && uv run ruff check . && uv run mypy src && uv run lint-imports
	cd frontend && npm run lint
