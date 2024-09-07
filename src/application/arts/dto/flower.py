from dataclasses import dataclass


@dataclass(frozen=True)
class DTOFlower:
    flower_name: str
    flower_path: str
