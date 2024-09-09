import asyncio

from src.domain.arts.events.arts import GetRandomArtEvent
from src.domain.flowers.events.flowers import GetRandomFlowerEvent
from src.domain.poems.events.poems import GetRandomPoemEvent
from src.infrastructure.di.main import init_container
from src.infrastructure.mediator.main import Mediator
from src.infrastructure.message_broker.base import BaseMessageBroker
from src.settings.config import Config


async def init_message_broker():
    container = init_container()
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    await message_broker.start()


async def consume_in_background():
    container = init_container()
    config: Config = container.resolve(Config)  # noqa
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)  # noqa

    mediator: Mediator = container.resolve(Mediator)  # noqa

    async def consume_art_topic():
        async for msg in message_broker.start_consuming(
            config.recieved_random_art_topic,
        ):
            await mediator.publish(
                [
                    GetRandomArtEvent(
                        art=msg["art"],
                        art_name=msg["art_name"],
                        art_direction=msg["art_direction"],
                        art_description=msg["art_description"],
                    ),
                ],
            )

    async def consume_poem_topic():
        async for msg in message_broker.start_consuming(
            config.recieved_random_poem_topic,
        ):
            await mediator.publish(
                [
                    GetRandomPoemEvent(
                        poem_title=msg["poem_title"],
                        poem_author=msg["poem_author"],
                        poem_text=msg["poem_text"],
                        poem_date=msg["poem_date"],
                    ),
                ],
            )

    async def consume_flower_topic():
        async for msg in message_broker.start_consuming(
            config.recieved_random_flower_topic,
        ):
            await mediator.publish(
                [
                    GetRandomFlowerEvent(
                        flower_name=msg["flower_name"],
                        flower_path=msg["flower_path"],
                    ),
                ],
            )

    await asyncio.gather(
        consume_art_topic(),
        consume_poem_topic(),
        consume_flower_topic(),
    )


async def close_message_broker():
    container = init_container()
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    await message_broker.close()
