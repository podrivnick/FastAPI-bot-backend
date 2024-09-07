from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BasePoemTitleException(ValueError, DomainException):
    """Base poem title exception."""

    @property
    def message(self):
        return "Invalid Poem Title."


@dataclass(eq=False)
class PoemTitleIsEmptyException(BasePoemTitleException):
    @property
    def message(self):
        return "Poem Title is empty."


@dataclass(eq=False)
class PoemTitleIsTooLongException(BasePoemTitleException):
    @property
    def message(self):
        return "Poem Title is too long."


@dataclass(eq=False)
class PoemTitleInCorrectFormatException(BasePoemTitleException):
    @property
    def message(self):
        return "Poem Title is incorrect format."
