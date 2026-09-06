"""
Main Application Entrypoint.

Initializes the core FastAPI application, loads environment variables, configures 
HTTP logging middleware, attaches domain routers (such as DICOM Toolkit), and 
exposes health/deployment readiness endpoints for Render.
"""
import os
from app.utils.logger import LoggingMiddleware
from fastapi import FastAPI, Response
from .routers.DICOMToolkit import dicom_toolkit
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

app = FastAPI(
    title="Multi-API SaaS Hub & DICOM Toolkit",
    description="Stateless microservice backend for medical imaging utilities.",
    version="0.1.0-beta",
)

# Middleware & Routing
app.include_router(dicom_toolkit.router)
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
def health_check():
    """
    HTTP endpoint path that Render messages periodically to monitor your service. 
    """
    return Response(status_code=200)
