from glob import glob
import os
import pytest

ANONIMIZED_TEST_DATA_RELATIVE_FOLDER = "../../../../test_data/Anonimized_DICOM/"

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

@pytest.mark.parametrize("modality, zip_file_path", get_zip_test_cases())
def test_get_modality_happy_path(client, modality, zip_file_path):
    """Test the metadata/get_metadata endpoint"""

    assert os.path.exists(zip_file_path), f"Test file not found: {zip_file_path}"

    with open(zip_file_path, "rb") as f:
        response = client.post(
            "/metadata/get_modality",
            files={"zipfile": (zip_file_path, f, "application/zip")},
        )

    assert response.status_code == 200
    assert response.json() == {"modality": modality}
