from app.main import HEALTHCHECK_RESPONSE

def test_main_happy_path(client):
    """Test the main '/' endpoint"""

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == HEALTHCHECK_RESPONSE
