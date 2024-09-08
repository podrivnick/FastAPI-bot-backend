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


async def close_message_broker():
    container = init_container()
    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)
    await message_broker.close()
