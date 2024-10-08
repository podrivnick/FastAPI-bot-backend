from dataclasses import (
    dataclass,
    field,
)


@dataclass(frozen=True)
class GetRandomFlowerSchema:
    get_random_flower_photo: bool | None = field(default=None)
