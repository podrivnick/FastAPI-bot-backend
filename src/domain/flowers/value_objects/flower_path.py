import re
from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.flowers import exceptions as ex


FLOWER_DESCRIPTION_PATTERN = re.compile(  # noqa: DUO138
    r"(\.\./|/)?([a-zA-Z0-9_\-\.]+/)*[a-zA-Z0-9_\-\.]+",
)  # Match relative or absolute file paths
MAX_LENGTH_FLOWERS_DESCRIPTION = 30


@dataclass(frozen=True)
class FlowerPath(ValueObject[str | None]):
    value: str | None

    def validate(
        self,
    ) -> None:
        if len(self.value) == 0:
            raise ex.FlowerPathIsEmptyException()

        if len(self.value) > MAX_LENGTH_FLOWERS_DESCRIPTION:
            raise ex.FlowerPathIsTooLongException()

        if not FLOWER_DESCRIPTION_PATTERN.match(self.value):
            raise ex.FlowerPathInCorrectFormatException()
