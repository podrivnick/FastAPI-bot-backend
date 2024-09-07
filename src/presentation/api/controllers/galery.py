from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from punq import Container
from src.application.arts.commands.arts import GetRandomArtCommand
from src.application.arts.commands.flowers import GetRandomFlowerCommand
from src.application.arts.dto.art import DTOArt
from src.application.arts.dto.flower import DTOFlower
from src.application.arts.dto.poem import DTOPoem
from src.application.arts.schemas.base import (
    GetRandomArtSchema,
    GetRandomFlowerSchema,
    GetRandomPoemByCertainAuthorSchema,
)
from src.domain.common.exceptions.base import BaseAppException
from src.infrastructure.di.main import init_container
from src.infrastructure.mediator.main import Mediator
from src.presentation.api.controllers.responses.base import (
    ErrorData,
    SuccessResponse,
)
from src.presentation.api.providers.stub import Stub


router = APIRouter(tags=["Galery"])


@router.post(
    "/random_art",
    status_code=status.HTTP_201_CREATED,
    description="Апи для получения случайной картины",
    responses={
        status.HTTP_201_CREATED: {"model": DTOArt},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorData},
    },
)
async def get_random_art_handler(
    schema: GetRandomArtSchema,
    container: Container = Depends(Stub(init_container)),
) -> SuccessResponse[DTOArt]:
    """Получить случайную картину из введённой категории."""
    mediator: Mediator = container.resolve(Mediator)

    try:
        art = await mediator.handle_command(
            GetRandomArtCommand(art_direction=schema.art_direction),
        )
    except BaseAppException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )

    return SuccessResponse(result=art)


@router.get(
    "/random_flower",
    status_code=status.HTTP_201_CREATED,
    description="Апи для получения случайного фото цветов",
    responses={
        status.HTTP_201_CREATED: {"model": DTOFlower},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorData},
    },
)
async def get_random_flower_handler(
    schema: GetRandomFlowerSchema = Depends(),
    container: Container = Depends(Stub(init_container)),
) -> SuccessResponse[DTOFlower]:
    """Получить случайное фото цветов."""
    mediator: Mediator = container.resolve(Mediator)

    try:
        flower = await mediator.handle_command(
            GetRandomFlowerCommand(),
        )
    except BaseAppException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )

    return SuccessResponse(result=flower)


@router.post(
    "/random_poem",
    status_code=status.HTTP_201_CREATED,
    description="Апи для получения случайного стихотворения",
    responses={
        status.HTTP_201_CREATED: {"model": DTOPoem},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorData},
    },
)
async def get_random_poem_handler(
    schema: GetRandomPoemByCertainAuthorSchema,
    container: Container = Depends(Stub(init_container)),
) -> SuccessResponse[DTOPoem]:
    """Получить случайное стихотворение полученного автора."""
    mediator: Mediator = container.resolve(Mediator)

    try:
        poem = await mediator.handle_command(
            GetRandomArtCommand(poem_author=schema.poem_author),
        )
    except BaseAppException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )

    return SuccessResponse(result=poem)
