
def test_get_modality(client):
    """Dummy test"""
    response = client.get("/metadata/modality")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
