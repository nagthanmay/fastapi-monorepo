# FastAPI Monorepo Template

## Overview

This is a scalable, production-ready FastAPI monorepo setup following modern software engineering practices. It includes:

- Monorepo structure with `apps/` and `libs/`
- PostgreSQL integration
- Alembic migrations
- Linting, type checking, pre-commit hooks
- JSON logging, request tracing, health checks
- API versioning, autogenerated docs

---

## Project Structure

- `apps/`: FastAPI applications
- `libs/`: Shared utilities like environment loaders
- `core/`: Config, logging, middleware, version tracking
- `db/`: ORM models, sessions, migrations
- `tests/`: Unit and integration tests

---

##  Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone <your-repo-url>
   cd fastapi-monorepo


##Code Skeleton 

Main App Logic

    main.py: Initializes FastAPI app, adds middleware, routers, exception handlers.

    health.py: Sample /v1/health endpoint.

Middleware

    middleware.py: Custom middleware for:

    Adding unique request IDs

    Tracking request duration

    Returning backend Git version

Environment Handling

    config.py: Loads and validates environment variables using Pydantic.

    env_loader.py: Utility used by config.py to read .env file.

Logging

    logging.py: Pretty logs in development and structured JSON logs in production.

Version Tracking

    version.py: Extracts Git commit SHA for traceability.

Exception Handling

    exceptions.py: Catches and returns formatted errors for HTTP and validation issues.

Database Integration

    base.py: Defines the SQLAlchemy base class.

    session.py: Sets up DB engine and sessionmaker.

    migrations/: Folder to store Alembic migration scripts.

Testing

    test_health.py: Verifies health endpoint returns 200 OK.

✨ Core Features Recap

    1.Deterministic dependency management using requirements.txt

    2.Dev/prod logging

    3.Middleware for trace IDs, request timing, and version headers

    4.Environment validation with .env

    5.Code quality: black, ruff, mypy, pre-commit hooks

    6.Centralized exception handling

    7.Versioned FastAPI routing with Swagger tags

    8.PostgreSQL integration with SQLAlchemy + Alembic

    9.Unit and integration test support

    10.GitHub Actions CI pipeline

Philosophy

Why Monorepo?

    Organizes multiple apps in apps/ and shared libraries in libs/

    Promotes modularity, reuse, and scalability

Developer Productivity

    Out-of-the-box features like versioning, logging, tracing, API docs, and env loading

    CI/CD and testing pre-integrated

Maintainability & Scalability

    Clear separation of concerns

    Configurable with modern tools

    Easy to scale into microservices


Run Tests
    pytest
Tooling
    Linting: ruff

Formatting: black

Typing: mypy

Pre-commit Hooks: Format, lint, validate messages

Git Hooks: Validate commit messages, enforce changelogs

API Features
    Versioned routing

    Health checks (/v1/health)

    JSON logs

Middleware for:

    Trace ID per request

    Response timing

    Backend Git version
Database
    ORM: SQLAlchemy 2.0 style

Migration: Alembic

Session Handling: Dependency-injected



Instructions on How to RUN

Step1: clone the Repo
git clone <https://github.com/nagthanmay/fastapi-monorepo.git>
cd fastapi-monorepo

Step2: Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate    # For Linux/macOS

# OR on Windows
venv\Scripts\activate

step3: install python dependencies
pip install -r requirements.txt

step4: 
Environment Variables
Create a .env file:

ENVIRONMENT=development
DATABASE_URL=postgresql://postgres:password@localhost:5432/app_db
APP_NAME=main_api

Step 5: Run Database Migrations (if any)
If you have Alembic configured with migrations:
alembic upgrade head
Otherwise, ensure your tables are created using SQLAlchemy models.

Step 6: Run the FastAPI App

uvicorn apps.main_api.main:app --reload
You should see output like:
INFO:     Uvicorn running on http://127.0.0.1:8000
Step 7: Access FastAPI Swagger Docs
Open your browser and navigate to:
Swagger UI: http://localhost:8000/docs

ReDoc UI: http://localhost:8000/redoc

These UIs are auto-generated by FastAPI from your route definitions and Pydantic schemas.

Troubleshooting Tips
If you see ModuleNotFoundError, make sure your folder structure matches the monorepo layout.

If your DB isn’t connecting, verify the DATABASE_URL and that your PostgreSQL server is running.

For errors on .env, confirm it is located at the root and named correctly.

