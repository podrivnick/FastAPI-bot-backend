from dataclasses import dataclass


@dataclass(frozen=True)
class DTOArt:
    art: str
    art_name: str
    art_direction: str
    art_description: str


@dataclass(frozen=True)
class DTOFlower:
    flower_name: str
    flower_path: str
