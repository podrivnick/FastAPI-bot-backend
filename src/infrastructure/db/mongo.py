from dataclasses import dataclass

from src.domain.arts.entities.art import Art
from src.domain.flowers.entities.flower import Flower
from src.infrastructure.db.config import BaseMongoDBRepository
from src.infrastructure.db.convertors import (
    convert_art_document_to_entity,
    convert_flower_document_to_entity,
)
from src.infrastructure.db.services import (
    BaseArtMongoDBService,
    BaseFlowerMongoDBService,
)


@dataclass
class ArtMongoDBService(BaseArtMongoDBService, BaseMongoDBRepository):
    async def get_random_art(
        self,
        art_direction: str,
    ) -> Art:
        pipeline = [
            {"$match": {"art_direction": art_direction}},
            {"$sample": {"size": 1}},
        ]
        cursor = self._collection.aggregate(pipeline)

        random_document = await cursor.to_list(length=1)

        return (
            convert_art_document_to_entity(random_document[0])
            if random_document
            else None
        )


@dataclass
class FlowerMongoDBService(BaseFlowerMongoDBService, BaseMongoDBRepository):
    async def get_random_flower(
        self,
    ) -> Flower:
        pipeline = [{"$sample": {"size": 1}}]
        cursor = self._collection.aggregate(pipeline)

        random_document = await cursor.to_list(length=1)
        print(random_document)
        return (
            convert_flower_document_to_entity(random_document[0])
            if random_document
            else None
        )
