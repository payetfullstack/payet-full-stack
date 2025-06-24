from fastapi import APIRouter, Depends

from ..dependencies import get_rapidapi_token_header

router = APIRouter(
    prefix="/metadata",
    tags=["metadata"],
    dependencies=[Depends(get_rapidapi_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/get_modality")
async def get_modality():
    return "CT"