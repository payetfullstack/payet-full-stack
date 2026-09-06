"""
ZIP Archive Security and Extraction Utilities.

Provides secure extraction of ZIP archives with built-in defenses against Zip Bomb 
attacks (file count and uncompressed size limits) and Zip Slip path traversal vulnerabilities.
"""
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
        zip_path (str): Path to the source ZIP file.
        extract_to (str): Destination directory where files should be extracted.

    Raises:
        ValueError: If file count exceeds limits, uncompressed size is too large, 
                    or unsafe path traversal is detected.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Check 1: File count limit
        file_count = len(zip_ref.namelist())
        if file_count > MAX_FILES:
            raise ValueError(f"Too many files in ZIP: {file_count} (max: {MAX_FILES})")

        # Check 2: Uncompressed size limit (Zip Bomb prevention)
        total_size = sum(zinfo.file_size for zinfo in zip_ref.infolist())
        max_bytes = MAX_TOTAL_SIZE_MB * 1024**2
        if total_size > max_bytes:
            raise ValueError(f"ZIP uncompressed size too large ({total_size / 1024**2:.1f} MB, max: {MAX_TOTAL_SIZE_MB} MB)")

        # Check 3: Zip Slip prevention & safe extraction
        for member in zip_ref.infolist():
            member_path = os.path.join(extract_to, member.filename)
            if not is_within_directory(extract_to, member_path):
                raise ValueError(f"Unsafe path detected in ZIP: {member.filename}")

        # Perform extraction safely
        zip_ref.extractall(extract_to)
