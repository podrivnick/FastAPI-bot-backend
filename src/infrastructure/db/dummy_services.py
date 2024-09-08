import random
from dataclasses import (
    dataclass,
    field,
)
from typing import List

from src.domain.arts.entities.art import Art
from src.domain.flowers.entities.flower import Flower
from src.domain.poems.entities.poem import Poem
from src.infrastructure.db.config import (
    get_saved_arts,
    get_saved_flowers,
    get_saved_poems,
)
from src.infrastructure.db.convertors import (
    convert_art_document_to_entity,
    convert_flower_document_to_entity,
    convert_poem_document_to_entity,
)
from src.infrastructure.db.services import (
    BaseArtMongoDBService,
    BaseFlowerMongoDBService,
    BasePoemMongoDBService,
)


@dataclass
class ArtMongoDummyService(BaseArtMongoDBService):
    _saved_arts: List[dict] = field(default_factory=list, kw_only=True)

    def __post_init__(self):
        self._saved_arts = get_saved_arts()

    async def get_random_art(
        self,
        art_direction: str,
    ) -> Art:
        filtered_arts = list(
            filter(
                lambda art: art.get("art_direction") == art_direction,
                self._saved_arts,
            ),
        )

        random_art = (
            random.SystemRandom.choice(filtered_arts) if filtered_arts else None
        )

        return convert_art_document_to_entity(random_art) if random_art else None


@dataclass
class FlowerMongoDummyService(BaseFlowerMongoDBService):
    _saved_flowers: List[dict] = field(default_factory=get_saved_flowers, kw_only=True)

    async def get_random_flower(
        self,
    ) -> Flower:
        random_flower = random.SystemRandom.choice(self._saved_flowers)

        return (
            convert_flower_document_to_entity(random_flower) if random_flower else None
        )


@dataclass
class PoemMongoDummyService(BasePoemMongoDBService):
    _saved_poems: List[dict] = field(default_factory=get_saved_poems, kw_only=True)

    async def get_random_poem(
        self,
        poem_author: str,
    ) -> Poem:
        filtered_poems = list(
            filter(
                lambda art: art.get("poem_author") == poem_author,
                self._saved_poems,
            ),
        )

        if filtered_poems:
            random_poem = random.SystemRandom.choise(filtered_poems)

        return convert_poem_document_to_entity(random_poem) if random_poem else None
