import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from apps.main_api.core.version import get_git_sha
import uuid

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Backend-Version"] = get_git_sha()
        response.headers["X-Response-Time"] = str(duration)
        return response

def add_middlewares(app: FastAPI):
    app.add_middleware(CustomMiddleware)