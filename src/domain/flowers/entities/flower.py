from dataclasses import dataclass
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.flowers import value_objects as vo
from src.domain.flowers.events.flowers import GetRandomFlowerEvent


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

        flower.record_event(
            GetRandomFlowerEvent(
                flower_name=flower_name.to_raw(),
                flower_path=flower_path.to_raw(),
            ),
        )

        return flower
