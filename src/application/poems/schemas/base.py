from dataclasses import dataclass


@dataclass(frozen=True)
class GetRandomPoemByCertainAuthorSchema:
    poem_author: str
