from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BasePoemAuthorException(ValueError, DomainException):
    """Base poem author exception."""

    @property
    def message(self):
        return "Invalid Poem Author"


@dataclass(eq=False)
class PoemAuthorIsEmptyException(BasePoemAuthorException):
    @property
    def message(self):
        return "Poem Author is empty"


@dataclass(eq=False)
class PoemAuthorIsTooLongException(BasePoemAuthorException):
    @property
    def message(self):
        return "Poem Author is too long"


@dataclass(eq=False)
class PoemAuthorInCorrectFormatException(BasePoemAuthorException):
    @property
    def message(self):
        return "Poem Author is incorrect format"
