up:
	docker compose up --build -d

down:
	docker compose down -v

dev:
	uv run fastapi dev app/main.py

lint:
	uv run ruff check --fix

format:
	uv run ruff format