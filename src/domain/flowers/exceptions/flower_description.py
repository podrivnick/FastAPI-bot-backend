from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BaseFlowerDescriptionException(ValueError, DomainException):
    """Base flower description exception."""

    @property
    def message(self):
        return "Invalid Flower Description"


@dataclass(eq=False)
class FlowerDescriptionIsEmptyException(BaseFlowerDescriptionException):
    @property
    def message(self):
        return "Invalid Flower is empty"


@dataclass(eq=False)
class FlowerDescriptionIsTooLongException(BaseFlowerDescriptionException):
    @property
    def message(self):
        return "Flower Description is too long"


@dataclass(eq=False)
class FlowerDescriptionInCorrectFormatException(BaseFlowerDescriptionException):
    @property
    def message(self):
        return "Flower Description is incorrect format"
