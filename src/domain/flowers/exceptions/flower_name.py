from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BaseFlowerNameException(ValueError, DomainException):
    """Base flower name exception."""

    @property
    def message(self):
        return "Invalid Flower Name"


@dataclass(eq=False)
class FlowerNameIsEmptyException(BaseFlowerNameException):
    @property
    def message(self):
        return "Flower name is empty"


@dataclass(eq=False)
class FlowerNameIsTooLongException(BaseFlowerNameException):
    @property
    def message(self):
        return "Flower Name is too long"


@dataclass(eq=False)
class FlowerNameInCorrectFormatException(BaseFlowerNameException):
    @property
    def message(self):
        return "Flower Name is incorrect format"
