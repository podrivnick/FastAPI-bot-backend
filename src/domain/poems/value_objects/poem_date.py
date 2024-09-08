import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.poems import exceptions as ex


POEM_DATE_PATTERN = re.compile(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$")  # noqa DUO138
MAX_LENGTH_POEM_DATE = 30


@dataclass(frozen=True)
class PoemDate(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.PoemDateIsEmptyException()

        if len(self.value) > MAX_LENGTH_POEM_DATE:
            raise ex.PoemDateIsTooLongException()

        if not POEM_DATE_PATTERN.match(self.value):
            raise ex.PoemDateInCorrectFormatException()
