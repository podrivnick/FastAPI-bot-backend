from dataclasses import dataclass

from domain.values.messages import Title
from infra.repositories.messages.base import BaseChatsRepository
from logic.commands.base import (
    BaseCommand,
    CommandHandler,
)
from logic.exceptions.messages import ChatWithThatTitleAlreadyExistsException
from src.domain.arts.entities.art import Art


@dataclass(frozen=True)
class GetRandomArtCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class GetRandomArtCommandHandler(CommandHandler[Art]):
    chats_repository: BaseChatsRepository

    async def handle(
        self,
        command: str,
    ) -> Art:
        if await self.chats_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExistsException(command.title)

        title = Title(value=command.title)

        new_chat = Art.create_chat(title=title)

        art = await self.chats_repository.add_chat(new_chat)

        return art
