from fastapi.testclient import TestClient
from app.dependencies import INVALID_HEADER_ERROR_MESSAGE
from app.main import HEALTHCHECK_RESPONSE
from ...main import app

def test_main_happy_path(client):
    """Test the main '/' endpoint"""

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == HEALTHCHECK_RESPONSE

def test_main_no_headers(client):
    """Test the main '/' endpoint without expected headers"""

    # No headers client
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 401
    assert response.json() == {'detail': INVALID_HEADER_ERROR_MESSAGE}
