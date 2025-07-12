from app.dependencies import get_rapidapi_token_header
from app.utils.logger import LoggingMiddleware
from fastapi import Depends, FastAPI
from .routers import metadata
from dotenv import load_dotenv

HEALTHCHECK_RESPONSE = {"message": "App is running"}

# Load env variables from .env
load_dotenv()

app = FastAPI()
app.include_router(metadata.router)
app.add_middleware(LoggingMiddleware)

@app.get("/", dependencies=[Depends(get_rapidapi_token_header)])
def read_root():
    return HEALTHCHECK_RESPONSE