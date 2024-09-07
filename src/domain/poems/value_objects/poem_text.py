import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.poems import exceptions as ex


POEM_TEXT_PATTERN = re.compile(r"(\.\./|/)?([a-zA-Z0-9_\-\.]+/)*[a-zA-Z0-9_\-\.]+")  # noqa DUO138
MAX_LENGTH_POEM_TEXT = 30


@dataclass(frozen=True)
class PoemText(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.PoemTextIsEmptyException()

        if len(self.value) > MAX_LENGTH_POEM_TEXT:
            raise ex.PoemTextIsTooLongException()

        if not POEM_TEXT_PATTERN.match(self.value):
            raise ex.PoemTextInCorrectFormatException()
