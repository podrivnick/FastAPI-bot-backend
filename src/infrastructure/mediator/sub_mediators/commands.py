from collections import defaultdict
from collections.abc import Iterable
from dataclasses import (
    dataclass,
    field,
)
from abc import ABC, abstractmethod
from src.domain.common.commands.base import BaseCommands
from src.domain.common.events.base import BaseEvent
from src.infrastructure.exceptions.mediator import (
    CommandHandlerNotRegisteredException,
    EventHandlerNotRegisteredException,
)
from src.infrastructure.mediator.handlers.commands import (
    CommandHandler,
    CR,
    CT,
)
from src.infrastructure.mediator.handlers.event import (
    ER,
    ET,
    EventHandler,
)


@dataclass(eq=False)
class CommandMediator(ABC):
    commands_map: dict[CR, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abstractmethod
    def register_command(
        self,
        command: CT,
        command_handlers: Iterable[CommandHandler[CT, CR]],
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def handle_command(
        self,
        command: BaseCommands
    )-> Iterable[CR]:
        raise NotImplementedError()
