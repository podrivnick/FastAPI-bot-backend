from dataclasses import dataclass
from typing import ClassVar

from src.domain.common.events.base import BaseEvent


@dataclass
class GetRandomPoemEvent(BaseEvent):
    event_title: ClassVar[str] = "Random Poem Recieved Event"

    poem_title: str
    poem_author: str
    poem_text: str
    poem_date: str
