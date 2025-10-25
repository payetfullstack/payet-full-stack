from glob import glob
import os

from app.routers.DICOMToolkit.dicomToolkit import DICOM_TOOLKIT_ENDPOINT_NAME
import pytest

ANONIMIZED_TEST_DATA_RELATIVE_FOLDER = "../../test_data/anonimized_dicom/"
BASE_URL = DICOM_TOOLKIT_ENDPOINT_NAME + "/metadata"


def get_zip_test_cases():
    base_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(base_dir, ANONIMIZED_TEST_DATA_RELATIVE_FOLDER))

    # Example result: [("CT", "/abs/path/CT/scan1.zip"), ("MR", "/abs/path/MR/scan2.zip")]
    test_cases = []
    for modality in ["CT", "MR", "PT", "US"]:
        modality_dir = os.path.join(root_dir, modality)
        zip_files = glob(os.path.join(modality_dir, "*.zip"))
        test_cases.extend([(modality, zip_file) for zip_file in zip_files])

    return test_cases

@pytest.mark.parametrize("modality, zip_file_path", get_zip_test_cases() or [("dummy", None)])
def test_get_modality_happy_path(client, modality, zip_file_path):
    """Test the dicom-toolkit/metadata/get-metadata endpoint"""

    assert zip_file_path is not None, "Please check test data location"
    assert os.path.exists(zip_file_path), f"Test file not found: {zip_file_path}"

    with open(zip_file_path, "rb") as f:
        response = client.post(
            f"{BASE_URL}/get-modality",
            files={"zipfile": (zip_file_path, f, "application/zip")},
        )

    assert response.status_code == 200, f"response.json(): {response.json()}"
    assert response.json() == {"modality": modality}
