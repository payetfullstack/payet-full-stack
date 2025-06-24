from fastapi import APIRouter, Depends

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/metadata",
    tags=["metadata"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/modality")
async def get_modality():
    return "CT"