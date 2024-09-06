from abc import ABC
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from uuid import uuid4

from src.domain.common.entities import Entity
from src.domain.common.events.base import Event


@dataclass
class AggregateRoot(Entity, ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    _events: list[Event] = field(
        default_factory=list,
        init=False,
        repr=False,
        hash=False,
        compare=False,
    )
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )

    def record_event(self, event: Event) -> None:
        self._events.append(event)

    def get_events(self) -> list[Event]:
        return self._events

    def clear_events(self) -> None:
        self._events.clear()

    def pull_events(self) -> list[Event]:
        events = self.get_events().copy()
        self.clear_events()
        return events
