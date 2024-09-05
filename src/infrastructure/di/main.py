from functools import lru_cache

from punq import (
    Container,
    Scope,
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

    config: Config = container.resolve(Config)  # noqa

    # Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(EventMediator, factory=init_mediator)

    return container
