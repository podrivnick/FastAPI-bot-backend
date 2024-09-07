from dataclasses import dataclass
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.flowers import value_objects as vo


@dataclass
class Flower(AggregateRoot):
    flower_name: vo.FlowerName
    flower_description: vo.FlowerDescription

    @classmethod
    def create_flower(
        cls,
        flower_name: vo.FlowerName,
        flower_description: vo.FlowerDescription,
    ) -> Self:
        flower = cls(
            flower_name=flower_name,
            flower_description=flower_description,
        )

        return flower
