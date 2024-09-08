from dataclasses import dataclass

from src.domain.common.commands.base import BaseCommands
from src.domain.poems import value_objects as poem_vo
from src.domain.poems.entities.poem import Poem
from src.infrastructure.db.services import BasePoemMongoDBService
from src.infrastructure.mediator.handlers.commands import CommandHandler


@dataclass(frozen=True)
class GetRandomPoemCommand(BaseCommands):
    poem_author: str


@dataclass(frozen=True)
class GetRandomPoemCommandHandler(CommandHandler[GetRandomPoemCommand, Poem]):
    poems_service: BasePoemMongoDBService

    async def handle(
        self,
        command: GetRandomPoemCommand,
    ) -> Poem:
        poem_author = poem_vo.PoemAuthor(command.poem_author)

        poem = await self.poems_service.get_random_poem(poem_author.to_raw())

        return poem
