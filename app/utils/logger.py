"""
HTTP Logging Middleware and Logger Setup.

Provides structured request/response logging for the DICOM Toolkit application,
measuring endpoint processing latency and status codes using a custom Starlette 
middleware component.
"""
from http import HTTPStatus
import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

# Configure application logger
logger = logging.getLogger("dicom_toolkit")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers if imported across multiple modules
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that records HTTP client access, request method, endpoint path,
    resulting status code with description, and total execution duration in seconds.
    """

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response: Response = await call_next(request)

        # Safely resolve HTTP status phrase without raising ValueError on non-standard codes
        try:
            status_phrase = HTTPStatus(response.status_code).phrase
        except ValueError:
            status_phrase = "Unknown Status"

        client_host = request.client.host if request.client else "unknown"
        elapsed_seconds = time.time() - start_time

        logger.info(
            f'{client_host} - "{request.method} {request.url.path}" '
            f'{response.status_code} {status_phrase} ({elapsed_seconds:.3f}s)'
        )

        return response
