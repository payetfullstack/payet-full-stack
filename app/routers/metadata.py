import os
from pickletools import pydict
from app.utils.dicom_utils import find_first_dicom
from app.utils.zip_utils import safe_extract_zip
from fastapi import APIRouter, Depends, UploadFile, HTTPException
import tempfile
from app.utils.logger import logger

from ..dependencies import get_rapidapi_token_header

router = APIRouter(
    prefix="/metadata",
    tags=["metadata"],
    dependencies=[Depends(get_rapidapi_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/get_modality")
async def get_modality(zipfile: UploadFile):
    """
    Extract the image modality of the given zip file.

    Args:
        zipfile: Zipfile containing DICOM volumens inside.
    """

    if not zipfile.filename.lower().endswith(".zip"):
        logger.error("Expected a ZIP file")
        raise HTTPException(status_code=400, detail="Expected a ZIP file")

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, zipfile.filename)

            # Save the uploaded ZIP in a temp folder
            with open(zip_path, "wb") as f:
                f.write(await zipfile.read())

            # Securely extract
            safe_extract_zip(zip_path, tmpdir)

            # Get a single DICOM
            dicom_data = find_first_dicom(tmpdir)
            if not dicom_data:
                logger.error("No valid DICOM found")
                raise HTTPException(status_code=400, detail="No valid DICOM found")

            modality = dicom_data.get("Modality", "Unknown")
            return {"modality": modality}

    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
