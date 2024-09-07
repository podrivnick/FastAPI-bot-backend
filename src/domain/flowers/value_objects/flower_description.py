import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.flowers import exceptions as ex


FLOWER_DESCRIPTION_PATTERN = re.compile(r"[A-Za-z][A-Za-z1-9_]+")
MAX_LENGTH_FLOWERS_DESCRIPTION = 30


@dataclass(frozen=True)
class FlowerDescription(ValueObject[str, None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.FlowerDescriptionIsEmptyException()

        if len(self.value) > MAX_LENGTH_FLOWERS_DESCRIPTION:
            raise ex.FlowerDescriptionIsTooLongException()

        if not FLOWER_DESCRIPTION_PATTERN.match(self.value):
            raise ex.FlowerDescriptionInCorrectFormatException()
