import os


def test_get_modality(client):
    """Test the metadata/get_metadata endpoint"""

    # Collect env variables for authentication from RapidAPI
    x_rapidapi_proxy_secret_name = os.getenv("X_RAPIDAPI_PROXY_SECRET_NAME", "MISSING X_RAPIDAPI_PROXY_SECRET_NAME")
    x_rapidapi_proxy_secret_value = os.getenv("X_RAPIDAPI_PROXY_SECRET_VALUE", "MISSING X_RAPIDAPI_PROXY_SECRET_VALUE")

    response = client.get(
        "/metadata/get_modality",
        headers={"X-Token": "expected-value", x_rapidapi_proxy_secret_name: x_rapidapi_proxy_secret_value}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
