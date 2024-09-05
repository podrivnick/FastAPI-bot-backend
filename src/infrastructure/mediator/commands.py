from src.domain.common.commands.base import BaseCommands
from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic


CT = TypeVar("CT", bound=BaseCommands)
CR = TypeVar("CR", bound=Any)


@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        raise NotImplementedError("Subclasses must implement handle method")
