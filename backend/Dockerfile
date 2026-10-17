FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.0 /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY alembic.ini ./
COPY migrations ./migrations
COPY app ./app

RUN mkdir -p /app/data

EXPOSE 8000
CMD ["sh", "-c", "uv run --no-dev alembic upgrade head && exec uv run --no-dev fastapi run app/main.py --host 0.0.0.0 --port 8000"]
