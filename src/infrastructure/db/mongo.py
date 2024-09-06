from dataclasses import dataclass

from src.infrastructure.db.config import BaseMongoDBRepository
from src.infrastructure.db.services import BaseMongoDBService


@dataclass
class ArtMongoDBService(BaseMongoDBService, BaseMongoDBRepository):
    async def get_random_art(self, art_direction: str) -> None:
        pipeline = [{"$sample": {"size": 1}}]
        cursor = self._collection.aggregate(pipeline)

        random_document = await cursor.to_list(length=1)

        return random_document[0] if random_document else None
