import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.poems import exceptions as ex


POEM_AUTHOR_PATTERN = re.compile(r"^[a-zA-Zа-яА-ЯёЁ0-9_\-\. ]+$")  # noqa DUO138
MAX_LENGTH_POEM_AUTHOR = 50


@dataclass(frozen=True)
class PoemAuthor(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.PoemAuthorIsEmptyException()

        if len(self.value) > MAX_LENGTH_POEM_AUTHOR:
            raise ex.PoemAuthorIsTooLongException()

        if not POEM_AUTHOR_PATTERN.match(self.value):
            raise ex.PoemAuthorInCorrectFormatException()
