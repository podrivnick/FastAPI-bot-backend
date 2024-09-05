from functools import lru_cache
from uuid import uuid4

from punq import (
    Container,
    Scope,
)
from src.infrastructure.mediator.handlers.event import (
    EventHandler,
)
from src.infrastructure.mediator.main import Mediator
from src.infrastructure.mediator.sub_mediators.event import EventMediator

from src.settings.config import Config
from src.infrastructure.mediator.main import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _initialize_container()


def _initialize_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)

    config: Config = container.resolve(Config)

    # Command handlers
    container.register(CreateChatCommandHandler)

    # Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        create_chat_handler = CreateChatCommandHandler(
            _mediator=mediator,
            chats_repository=container.resolve(BaseChatRepository),
        )

        # commands
        mediator.register_command(
            CreateChatCommand,
            [create_chat_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(EventMediator, factory=init_mediator)

    return container
