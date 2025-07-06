import pytest
import os
from fastapi.testclient import TestClient
from ...main import app

class AuthenticatedClient(TestClient):
    def request(self, method, url, **kwargs):
        # Collect env variables
        x_rapidapi_proxy_secret_name = os.getenv("X_RAPIDAPI_PROXY_SECRET_NAME", "X-RapidAPI-Proxy-Secret")
        x_rapidapi_proxy_secret_value = os.getenv("X_RAPIDAPI_PROXY_SECRET_VALUE", "default-secret")

        # Inject headers
        headers = kwargs.pop("headers", {}) or {}
        headers[x_rapidapi_proxy_secret_name] = x_rapidapi_proxy_secret_value

        return super().request(method, url, headers=headers, **kwargs)


@pytest.fixture
def client():
    # Client will always use the X_RAPIDAPI_PROXY headers
    client = AuthenticatedClient(app)
    yield client
