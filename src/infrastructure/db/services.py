from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class BaseMongoDBService(ABC):
    @abstractmethod
    async def get_random_art(self) -> None:
        raise NotImplementedError()
