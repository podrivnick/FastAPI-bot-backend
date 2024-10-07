from dataclasses import dataclass

from src.domain.arts.exceptions.art_name import ArtNameIsEmptyException
from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class ArtName(ValueObject[str | None]):
    value: str | None

    def validate(self) -> None:
        if len(self.value) == 0:
            raise ArtNameIsEmptyException()

    def exists(self) -> bool:
        return self.value is not None
