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

        logger.info(
            f"📥 Incoming request:\n"
            f"→ {request.method} {request.url.path}\n"
            f"→ From: {request.client.host if request.client else "unknown"}\n"
        )

        response: Response = await call_next(request)

        logger.info(
            f"📤 Response:\n"
            f"→ Status: {response.status_code}\n"
            f"→ Duration: {(time.time() - start_time):.3f}s"
        )
        return response
