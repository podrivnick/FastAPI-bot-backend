from fastapi import (
    APIRouter,
    Depends,
    status,
)
from punq import Container
from src.infrastructure.di.main import init_container
from src.infrastructure.mediator.main import Mediator
from src.presentation.api.controllers.test import (
    CreateChatCommand,
    CreateSchemaTest,
)
from starlette.responses import RedirectResponse


default_router = APIRouter(
    prefix="",
    tags=["default"],
    include_in_schema=True,
)


@default_router.get("/")
async def default_redirect() -> RedirectResponse:
    return RedirectResponse(
        "/docs",
        status_code=status.HTTP_302_FOUND,
    )


@default_router.post(
    "/create_schema",
    response_model=dict,
)
async def create_schemas(
    schema: CreateSchemaTest,
    container: Container = Depends(init_container),
):
    mediator: Mediator = container.resolve(Mediator)

    schemas, *_ = await mediator.handle_command(
        CreateChatCommand(name=schema.name, surname=schema.surname),
    )

    return {
        "message": "Created schemas",
        "schemas": schemas,
        "count": len(schemas) if schemas else 0,
        "success": schemas is not None,
        "status_code": status.HTTP_200_OK,
        "error": None,
    }
