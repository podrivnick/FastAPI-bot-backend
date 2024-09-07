from dataclasses import dataclass
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.flowers import value_objects as vo


@dataclass
class Flower(AggregateRoot):
    flower_name: vo.FlowerName
    flower_path: vo.FlowerPath

    @classmethod
    def create_flower(
        cls,
        flower_name: vo.FlowerName,
        flower_path: vo.FlowerPath,
    ) -> Self:
        flower = cls(
            flower_name=flower_name,
            flower_path=flower_path,
        )

        return flower
