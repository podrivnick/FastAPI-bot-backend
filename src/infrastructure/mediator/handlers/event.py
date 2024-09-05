from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Generic,
    TypeVar,
)

from src.domain.common.events.base import BaseEvent


ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    @abstractmethod
    def handle(self, ET) -> ER:
        raise NotImplementedError()
