from functools import lru_cache
from uuid import uuid4

from aiojobs import Scheduler
from aiokafka import (
    AIOKafkaConsumer,
    AIOKafkaProducer,
)
from motor.motor_asyncio import AsyncIOMotorClient
from punq import (
    Container,
    Scope,
)
from src.application.arts.commands.arts import (
    GetRandomArtCommand,
    GetRandomArtCommandHandler,
)
from src.application.arts.events.arts import (
    ArtReceivedFromBrokerEvent,
    ArtReceivedFromBrokerEventHandler,
    GetRandomArtEventHandler,
)
from src.application.flowers.commands.flowers import (
    GetRandomFlowerCommand,
    GetRandomFlowerCommandHandler,
)
from src.application.poems.commands.poems import (
    GetRandomPoemCommand,
    GetRandomPoemCommandHandler,
)
from src.domain.arts.events.arts import GetRandomArtEvent
from src.infrastructure.db.mongo import (
    ArtMongoDBService,
    FlowerMongoDBService,
    PoemMongoDBService,
)
from src.infrastructure.db.services import (
    BaseArtMongoDBService,
    BaseFlowerMongoDBService,
    BasePoemMongoDBService,
)
from src.infrastructure.mediator.main import Mediator
from src.infrastructure.mediator.sub_mediators.event import EventMediator
from src.infrastructure.message_broker.base import BaseMessageBroker
from src.infrastructure.message_broker.kafka import KafkaMessageBroker
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

    def init_mongodb_poems_service() -> BasePoemMongoDBService:
        return PoemMongoDBService(
            mongo_db_client=client,
            mongo_db_db_name=config.mongodb_galery_database,
            mongo_db_collection=config.mongodb_poems_collection,
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

    container.register(
        BasePoemMongoDBService,
        factory=init_mongodb_poems_service,
        scope=Scope.singleton,
    )

    # Handlers
    container.register(GetRandomArtCommandHandler)
    container.register(GetRandomFlowerCommandHandler)
    container.register(GetRandomPoemCommandHandler)

    # Kafka
    def create_message_broker() -> BaseMessageBroker:
        return KafkaMessageBroker(
            producer=AIOKafkaProducer(bootstrap_servers=config.kafka_url),
            consumer=AIOKafkaConsumer(
                bootstrap_servers=config.kafka_url,
                group_id=f"galery-{uuid4()}",
                metadata_max_age_ms=1000000,
            ),
        )

    container.register(
        BaseMessageBroker,
        factory=create_message_broker,
        scope=Scope.singleton,
    )

    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        get_random_art_handler = GetRandomArtCommandHandler(
            _mediator=mediator,
            arts_service=container.resolve(BaseArtMongoDBService),
        )

        # command handlers
        get_random_flower_handler = GetRandomFlowerCommandHandler(
            _mediator=mediator,
            flowers_service=container.resolve(BaseFlowerMongoDBService),
        )

        # command handlers
        get_random_poem_handler = GetRandomPoemCommandHandler(
            _mediator=mediator,
            poems_service=container.resolve(BasePoemMongoDBService),
        )

        # event handlers
        random_art_handler_event = GetRandomArtEventHandler(
            broker_topic=config.recieved_random_art_topic,
            message_broker=container.resolve(BaseMessageBroker),
        )

        # event handlers
        random_art_received_from_broker_event_handler = (
            ArtReceivedFromBrokerEventHandler(
                message_broker=container.resolve(BaseMessageBroker),
                broker_topic=config.recieved_random_art_topic,
            )
        )

        # events
        mediator.register_events(
            GetRandomArtEvent,
            [random_art_handler_event],
        )
        # events
        mediator.register_events(
            ArtReceivedFromBrokerEvent,
            [random_art_received_from_broker_event_handler],
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

        # commands
        mediator.register_command(
            GetRandomPoemCommand,
            [get_random_poem_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(EventMediator, factory=init_mediator)

    container.register(Scheduler, factory=lambda: Scheduler(), scope=Scope.singleton)

    return container
