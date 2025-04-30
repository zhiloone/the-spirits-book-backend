up:
	docker compose up --build -d

down:
	docker compose down -v

dev:
	uv run fastapi dev app/main.py

seed:
	PYTHONPATH=. uv run app/database/seed_questions/seed_questions.py

lint:
	uv run ruff check --fix

format:
	uv run ruff format