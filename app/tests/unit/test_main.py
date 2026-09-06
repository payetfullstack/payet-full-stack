"""
Root and Health Check Endpoint Tests.

Contains test cases verifying core system availability, including the 
root endpoints ('/') via GET and HEAD requests, as well as application 
health checks ('/healthz').
"""
from ...main import app

def test_get_main_root_happy_path(client):
    """Test the main_root '/' endpoint with a GET request"""

    response = client.get("/")
    assert response.status_code == 200

def test_head_main_root_happy_path(client):
    """Test the main_root '/' endpoint with a HEAD request"""

    response = client.head("/")
    assert response.status_code == 200
    # HEAD responses must not contain a body
    assert len(response.content) == 0

def test_health_happy_path(client):
    """Test the healthz '/healthz' endpoint with a GET request"""

    response = client.get("/healthz")
    assert response.status_code == 200
