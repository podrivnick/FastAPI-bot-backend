from src.domain.common.exceptions.base import BaseAppException
from dataclasses import dataclass


@dataclass(frozen=True)
class EventHandlerNotRegisteredException(BaseAppException):
    @property
    def message(self) -> str:
        return "Event handler not registered for the given event"


@dataclass(frozen=True)
class CommandHandlerNotRegisteredException(BaseAppException):
    @property
    def message(self) -> str:
        return "Command handler not registered for the given event"
