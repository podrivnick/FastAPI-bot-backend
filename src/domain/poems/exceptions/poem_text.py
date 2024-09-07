from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BasePoemTextException(ValueError, DomainException):
    """Base poem text exception."""

    @property
    def message(self):
        return "Invalid Poem Text"


@dataclass(eq=False)
class PoemTextIsEmptyException(BasePoemTextException):
    @property
    def message(self):
        return "Poem Text is empty"


@dataclass(eq=False)
class PoemTextIsTooLongException(BasePoemTextException):
    @property
    def message(self):
        return "Poem Text is too long"


@dataclass(eq=False)
class PoemTextInCorrectFormatException(BasePoemTextException):
    @property
    def message(self):
        return "Poem Text is incorrect format"
