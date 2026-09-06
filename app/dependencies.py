"""
Authentication and Authorization Dependencies.
"""
from fastapi import HTTPException, Request
import os

INVALID_HEADER_ERROR_MESSAGE = "Invalid header"

async def get_rapidapi_token_header(request: Request):
    """
    Check if the expected RapidAPI headers are found in request header.

    Raises:
        401: Invalid header
        500: If env variables not configured
    """
    # Extract all headers
    all_headers = dict(request.headers)

    x_rapidapi_proxy_secret_name = os.getenv("X_RAPIDAPI_PROXY_SECRET_NAME", None)
    x_rapidapi_proxy_secret_value = os.getenv("X_RAPIDAPI_PROXY_SECRET_VALUE", None)

    if not x_rapidapi_proxy_secret_name or not x_rapidapi_proxy_secret_value:
        raise HTTPException(status_code=500, detail="Env variables wrongly configured!")

    rapidapi_secret = all_headers.get(x_rapidapi_proxy_secret_name.lower(), None)

    if not rapidapi_secret or rapidapi_secret !=  x_rapidapi_proxy_secret_value:
        raise HTTPException(status_code=401, detail=INVALID_HEADER_ERROR_MESSAGE)
