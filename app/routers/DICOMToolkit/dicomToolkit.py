from fastapi import APIRouter, Depends
from . import metadata
from ...dependencies import get_rapidapi_token_header

DICOM_TOOLKIT_ENDPOINT_NAME = "dicom-toolkit"

router = APIRouter(
    prefix=f"/{DICOM_TOOLKIT_ENDPOINT_NAME}",
    tags=[DICOM_TOOLKIT_ENDPOINT_NAME],
    dependencies=[Depends(get_rapidapi_token_header)],
    responses={404: {"description": "Not found"}},
)
router.include_router(metadata.router)