from dataclasses import (
    dataclass,
    field,
)

from src.domain.common.commands.base import BaseCommands
from src.domain.flowers.entities.flower import Flower
from src.infrastructure.db.services import BaseFlowerMongoDBService
from src.infrastructure.mediator.handlers.commands import CommandHandler


@dataclass(frozen=True)
class GetRandomFlowerCommand(BaseCommands):
    flower: str | None = field(default=None)


@dataclass(frozen=True)
class GetRandomFlowerCommandHandler(CommandHandler[GetRandomFlowerCommand, Flower]):
    flowers_service: BaseFlowerMongoDBService

    async def handle(
        self,
        command: GetRandomFlowerCommand,
    ) -> Flower:
        flower = await self.flowers_service.get_random_flower()

        return flower
