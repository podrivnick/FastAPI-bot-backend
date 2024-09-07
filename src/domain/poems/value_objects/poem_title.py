import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.poems import exceptions as ex


POEM_TITLE_PATTERN = re.compile(r"(\.\./|/)?([a-zA-Z0-9_\-\.]+/)*[a-zA-Z0-9_\-\.]+")  # noqa DUO138
MAX_LENGTH_POEM_TITLE = 30


@dataclass(frozen=True)
class PoemTitle(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.PoemTitleIsEmptyException()

        if len(self.value) > MAX_LENGTH_POEM_TITLE:
            raise ex.PoemTitleIsTooLongException()

        if not POEM_TITLE_PATTERN.match(self.value):
            raise ex.PoemTitleInCorrectFormatException()
