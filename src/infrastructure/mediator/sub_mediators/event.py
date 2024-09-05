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
class EventMediator(ABC):
    event_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abstractmethod
    def register_events(
        self,
        event: ET,
        event_handlers: Iterable[EventHandler[ET, ER]],
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def publish_event(
        self,
        events: Iterable[BaseEvent]
    ) -> Iterable[ER]:
        raise NotImplementedError()
