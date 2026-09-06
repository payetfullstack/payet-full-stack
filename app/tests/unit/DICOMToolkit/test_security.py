"""
Authentication and Security Tests for all the DICOM Toolkit Endpoints.
"""
from fastapi.testclient import TestClient

from app.routers.DICOMToolkit.dicom_toolkit import DICOM_TOOLKIT_ENDPOINT_NAME
from ....main import app


def test_dicom_toolkit_endpoints_require_auth():
    """
    Automatically test that all /dicom-toolkit/* endpoints require
    RapidAPI headers by checking that unauthorized requests return 401.
    """
    # Client without RapidAPI headers
    client = TestClient(app)

    for route in app.routes:
        if not hasattr(route, "methods"):
            continue

        path = route.path
        methods = route.methods

        if not path.startswith(f"/{DICOM_TOOLKIT_ENDPOINT_NAME}"):
            continue

        for method in methods:
            response = client.request(method, path)
            assert response.status_code == 401, (
                f"{method} {path} did not return 401, got {response.status_code}: {response.json()}"
            )
