from fastapi import FastAPI
from .routers import metadata

app = FastAPI()
app.include_router(metadata.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
