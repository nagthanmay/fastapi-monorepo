from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from apps.main_api.api.v1.endpoints import health
from apps.main_api.core import middleware, config, logging as log_config, exceptions

log_config.setup_logging()

app = FastAPI(title="Main API", version="1.0.0")

middleware.add_middlewares(app)
app.include_router(health.router, prefix="/v1/health", tags=["Health"])

# Register exception handlers
app.add_exception_handler(StarletteHTTPException, exceptions.http_exception_handler)
app.add_exception_handler(RequestValidationError, exceptions.validation_exception_handler)