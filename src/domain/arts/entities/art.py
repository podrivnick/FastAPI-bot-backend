from dataclasses import dataclass
from typing import Self

from src.domain.arts import value_objects as vo
from src.domain.common.entities.aggregate_root import AggregateRoot


@dataclass
class Art(AggregateRoot):
    art: vo.Art
    art_name: vo.ArtName
    art_direction: vo.ArtDirection
    art_description: vo.ArtDescription

    @classmethod
    def create_art(
        cls,
        art: vo.Art,
        art_name: vo.ArtName,
        art_direction: vo.ArtDirection,
        art_description: vo.ArtDescription,
    ) -> Self:
        art = cls(
            art=art,
            art_name=art_name,
            art_direction=art_direction,
            art_description=art_description,
        )

        return art
