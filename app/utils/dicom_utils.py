import os
import pydicom

def find_first_dicom(directory: str, stop_before_pixels=True):
    """
    Get the first DICOM file from folder. None if not found

    directory: Path to the folder to evaluate
    stop_before_pixels: Boolean to indicate if image pixels should be excluded (true) or not (false)
    """
    for root, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                dicom_data = pydicom.dcmread(file_path, stop_before_pixels=stop_before_pixels)
                return dicom_data
            except Exception:
                continue
    return None
