.PHONY: install test lint format run-fastapi docker-up docker-down

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .
	mypy .

format:
	ruff format .

run-fastapi:
	uvicorn examples.production-api-fastapi.app.main:app --reload --host 0.0.0.0 --port 8000

docker-up:
	docker compose up --build

docker-down:
	docker compose down -v
