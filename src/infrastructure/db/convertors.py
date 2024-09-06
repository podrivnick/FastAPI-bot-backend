from typing import (
    Any,
    Mapping,
)

from src.domain.arts import value_objects as vo
from src.domain.arts.entities.art import Art


def convert_art_document_to_entity(message_document: Mapping[str, Any]) -> Art:
    return Art(
        art=vo.Art(message_document["art"]),
        art_name=vo.ArtName(message_document["art_name"]),
        art_direction=vo.ArtDirection(message_document["art_direction"]),
        art_description=vo.ArtDescription(message_document["art_description"]),
    )
