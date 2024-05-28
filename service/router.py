from fastapi import APIRouter, Depends, UploadFile
from starlette import status

from service.dependencies import bird_service_dependency
from service.schema import Bird
from service.service import BirdService

router = APIRouter()


@router.post("/get-bird", status_code=status.HTTP_200_OK, response_model=Bird)
async def get_bird(
    file: UploadFile,
    service: BirdService = Depends(bird_service_dependency)
):
    return await service.get_bird(file)
