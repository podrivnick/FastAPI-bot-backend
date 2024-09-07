from dataclasses import (
    dataclass,
    field,
)


@dataclass(frozen=True)
class GetRandomArtSchema:
    art_direction: str


@dataclass(frozen=True)
class GetRandomFlowerSchema:
    get_random_flower_photo: bool | None = field(default=None)


@dataclass(frozen=True)
class GetRandomPoemByCertainAuthorSchema:
    poem_author: str
