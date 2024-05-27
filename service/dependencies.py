from service.service import BirdService


async def bird_service_dependency() -> BirdService:
    return BirdService()
