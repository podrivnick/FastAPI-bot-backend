import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.poems import exceptions as ex


POEM_TEXT_PATTERN = re.compile(  # noqa DUO138
    r"^(?!\s*$)(?:.*\n?)*$",
    re.MULTILINE,
)  # noqa DUO138


@dataclass(frozen=True)
class PoemText(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.PoemTextIsEmptyException()

        if not POEM_TEXT_PATTERN.match(self.value):
            raise ex.PoemTextInCorrectFormatException()
