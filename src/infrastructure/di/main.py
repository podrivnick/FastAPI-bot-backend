from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient
from punq import (
    Container,
    Scope,
)
from src.application.arts.commands.arts import (
    GetRandomArtCommand,
    GetRandomArtCommandHandler,
)
from src.application.arts.commands.flowers import (
    GetRandomFlowerCommand,
    GetRandomFlowerCommandHandler,
)
from src.infrastructure.db.mongo import (
    ArtMongoDBService,
    FlowerMongoDBService,
)
from src.infrastructure.db.services import (
    BaseArtMongoDBService,
    BaseFlowerMongoDBService,
)
from src.infrastructure.mediator.main import Mediator
from src.infrastructure.mediator.sub_mediators.event import EventMediator
from src.settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _initialize_container()


def _initialize_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)

    config: Config = container.resolve(Config)

    def create_mongo_async_client():
        return AsyncIOMotorClient(
            config.mongo_db_connection_uri,
            serverSelectionTimeoutMS=3000,
        )

    container.register(
        AsyncIOMotorClient,
        factory=create_mongo_async_client,
        scope=Scope.singleton,
    )
    client = container.resolve(AsyncIOMotorClient)

    def init_mongodb_arts_service() -> BaseArtMongoDBService:
        return ArtMongoDBService(
            mongo_db_client=client,
            mongo_db_db_name=config.mongodb_galery_database,
            mongo_db_collection=config.mongodb_arts_collection,
        )

    def init_mongodb_flowers_service() -> BaseFlowerMongoDBService:
        return FlowerMongoDBService(
            mongo_db_client=client,
            mongo_db_db_name=config.mongodb_galery_database,
            mongo_db_collection=config.mongodb_flowers_collection,
        )

    container.register(
        BaseArtMongoDBService,
        factory=init_mongodb_arts_service,
        scope=Scope.singleton,
    )

    container.register(
        BaseFlowerMongoDBService,
        factory=init_mongodb_flowers_service,
        scope=Scope.singleton,
    )

    # Handlers
    container.register(GetRandomArtCommandHandler)
    container.register(GetRandomFlowerCommandHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        get_random_art_handler = GetRandomArtCommandHandler(
            arts_service=container.resolve(BaseArtMongoDBService),
        )

        # command handlers
        get_random_flower_handler = GetRandomFlowerCommandHandler(
            flowers_service=container.resolve(BaseFlowerMongoDBService),
        )

        # commands
        mediator.register_command(
            GetRandomArtCommand,
            [get_random_art_handler],
        )

        # commands
        mediator.register_command(
            GetRandomFlowerCommand,
            [get_random_flower_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(EventMediator, factory=init_mediator)

    return container
