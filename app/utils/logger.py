from http import HTTPStatus
import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


logger = logging.getLogger("dicom_toolkit")
logger.setLevel(logging.INFO)


# Avoid duplicate handlers
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# Middleware to always display a log at the begining and end of a request
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response: Response = await call_next(request)

        logger.info((
            f"{request.client.host if request.client else 'unknown'} - "
            f"\"{request.method} {request.url.path}\" "
            f"{response.status_code} {HTTPStatus(response.status_code).phrase} ({(time.time() - start_time):.3f})"
        ))
        return response
