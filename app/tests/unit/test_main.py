from ...main import app

def test_get_main_root_happy_path(client):
    """Test the main_root '/' endpoint with a GET request"""

    response = client.get("/")
    assert response.status_code == 200

def test_head_main_root_happy_path(client):
    """Test the main_root '/' endpoint with a HEAD request"""

    for route in app.routes:
        print(f"Route: {route.path}, methods: {route.methods}")

    response = client.head("/")
    assert response.status_code == 200

def test_health_happy_path(client):
    """Test the healthz '/healthz' endpoint with a GET request"""

    response = client.get("/healthz")
    assert response.status_code == 200