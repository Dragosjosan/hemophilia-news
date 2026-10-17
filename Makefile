.PHONY: install test lint migrate seed

.DEFAULT_GOAL := help

COMPOSE := docker compose -f docker-compose.yml

help:
	@echo "Development:"
	@echo "  make build-fe - build fe locally"
	@echo ""

install:
	cd backend && uv sync
	cd agents/maf && uv sync
	cd frontend && bun install

migrate:
	cd backend && uv run alembic upgrade head

seed: migrate
	cd backend && uv run python -m app.db.seed

test:
	cd backend && uv run pytest
	cd agents/maf && uv run pytest
	cd frontend && bun run build

lint:
	cd backend && uv run ruff check . && uv run mypy app
	cd agents/maf && uv run ruff check . && uv run mypy src
	cd frontend && bun run lint

build:
	$(COMPOSE) build

run:
	$(COMPOSE) up -d --remove-orphans

down:
	$(COMPOSE) down

