from dataclasses import dataclass

from src.domain.common.exceptions.base import DomainException


@dataclass(eq=False)
class BasePoemDateException(ValueError, DomainException):
    """Base poem date exception."""

    @property
    def message(self):
        return "Invalid Poem Date"


@dataclass(eq=False)
class PoemDateIsEmptyException(BasePoemDateException):
    @property
    def message(self):
        return "Poem Date is empty"


@dataclass(eq=False)
class PoemDateIsTooLongException(BasePoemDateException):
    @property
    def message(self):
        return "Poem Date is too long"


@dataclass(eq=False)
class PoemDateInCorrectFormatException(BasePoemDateException):
    @property
    def message(self):
        return "Poem Date is incorrect format"
