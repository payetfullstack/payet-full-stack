import os
from app.utils.logger import LoggingMiddleware
from fastapi import FastAPI, Response
from .routers import metadata
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

app = FastAPI()
app.include_router(metadata.router)

# Common logs fore each request. Already in Render
if os.getenv("DEBUG_MODE", 0):
    app.add_middleware(LoggingMiddleware)


@app.head("/")
@app.get("/")
def main_root():
    """
    Root endpoint is used by Render to verify that the server is running
    at deploy time.
    Reder calls both the HEAD and GET endpoints, so we need to manage both.
    """
    return Response(status_code=200)


@app.get("/healthz")
def main_root():
    """
    HTTP endpoint path that Render messages periodically to monitor your service. 
    """
    return Response(status_code=200)
