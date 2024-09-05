import logging

from collections import defaultdict
from collections.abc import Iterable
from src.infrastructure.mediator.event import EventHandler
from src.domain.common.events.base import BaseEvent
from typing import Any
from src.domain.common.commands.base import BaseCommands
from src.infrastructure.mediator.commands import CommandHandler, CT, CR
from src.infrastructure.exceptions.base import EventHandlerNotRegisteredException, CommandHandlerNotRegisteredException


@dataclass(frozen=True)
class Mediator:
    event_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    commands_map: dict[CR, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    def register_events(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]) -> None:
        self.event_map[event].append(event_handlers)

    def register_command(self, command: CT, command_handlers: Iterable[CommandHandler[CT, CR]]) -> None:
        self.event_map[command].extend(command_handlers)

    async def publish_event(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        event_type = events.__class__
        handlers = self.event_map.get(event_type)

        if not handlers:
            raise EventHandlerNotRegisteredException()

        results = []

        for event in events:
            results.extend([await handler.handle(event) for handler in handlers])

        return result

    async def handle_command(self, command: BaseCommands) -> Iterable[CR]:
        event_type = command.__class__
        handlers = self.event_map.get(event_type)

        if not handlers:
            raise CommandHandlerNotRegisteredException()

        return [await handler.handle(command) for handler in handlers]
