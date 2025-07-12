from app.utils.logger import LoggingMiddleware
from fastapi import FastAPI
from .routers import metadata
from dotenv import load_dotenv


# Load env variables from .env
load_dotenv()

app = FastAPI()
app.include_router(metadata.router)
app.add_middleware(LoggingMiddleware)