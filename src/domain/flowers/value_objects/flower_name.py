import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.flowers import exceptions as ex


FLOWER_NAME_PATTERN = re.compile(r"[A-Za-z][A-Za-z1-9_]+")
MAX_LENGTH_FLOWERS_NAME = 30


@dataclass(frozen=True)
class FlowerName(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.FlowerNameIsEmptyException()

        if len(self.value) > MAX_LENGTH_FLOWERS_NAME:
            raise ex.FlowerNameIsTooLongException()

        # if not FLOWER_NAME_PATTERN.match(self.value):
        #     raise ex.FlowerNameInCorrectFormatException()
