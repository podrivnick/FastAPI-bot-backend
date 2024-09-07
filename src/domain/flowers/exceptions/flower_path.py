from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BaseFlowerPathException(ValueError, DomainException):
    """Base flower path exception."""

    @property
    def message(self):
        return "Invalid Flower Path"


@dataclass(eq=False)
class FlowerPathIsEmptyException(BaseFlowerPathException):
    @property
    def message(self):
        return "Flower Path is empty"


@dataclass(eq=False)
class FlowerPathIsTooLongException(BaseFlowerPathException):
    @property
    def message(self):
        return "Flower Path is too long"


@dataclass(eq=False)
class FlowerPathInCorrectFormatException(BaseFlowerPathException):
    @property
    def message(self):
        return "Flower Path is incorrect format"
