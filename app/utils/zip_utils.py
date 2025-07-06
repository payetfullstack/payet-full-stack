import os
import zipfile


MAX_FILES = 800
MAX_TOTAL_SIZE_MB = 800


def is_within_directory(base_dir: str, target_path: str) -> bool:
    """
    Checks if the two paths are in the same folder.

    base_dir Path to evaluate
    target_path: Path to evaluate
    """
    abs_base = os.path.abspath(base_dir)
    abs_target = os.path.abspath(target_path)
    return os.path.commonpath([abs_base]) == os.path.commonpath([abs_base, abs_target])

def safe_extract_zip(zip_path: str, extract_to: str):
    """
    Extract the files inside a zip file. Block files too big.
    Args:
        zip_path: Path to the zip file to extract.
        extract_to: Path where to extract the file.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        if len(zip_ref.namelist()) > MAX_FILES:
            raise ValueError(f"Too many files in ZIP: {len(zip_ref.namelist())}")

        total_size = sum(zinfo.file_size for zinfo in zip_ref.infolist())
        if total_size > MAX_TOTAL_SIZE_MB * 1024**2:
            raise ValueError(f"ZIP too large {total_size / 1024**2} MB")

        for member in zip_ref.namelist():
            member_path = os.path.join(extract_to, member)
            if not is_within_directory(extract_to, member_path):
                raise ValueError("Unsafe path in ZIP")
        
        zip_ref.extractall(extract_to)
