from app.utils.logger import LoggingMiddleware
from fastapi import FastAPI, Response
from .routers import metadata
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

app = FastAPI()
app.include_router(metadata.router)
app.add_middleware(LoggingMiddleware)


@app.head('/')
@app.get("/")
def main_root():
    """
    Root endpoint is used by Render to verify that the server is running.
    Reder calls both the HEAD and GET endpoints, so we need to manage both
    """
    return Response(status_code=200)