run:
	uvicorn apps.main_api.main:app --reload

migrate:
	alembic upgrade head

lint:
	ruff .
	mypy .

format:
	black .