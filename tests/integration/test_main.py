from fastapi.testclient import TestClient
from main import app  # your FastAPI app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # adapt to your response
