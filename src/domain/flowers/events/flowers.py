from dataclasses import dataclass
from typing import ClassVar

from src.domain.common.events.base import BaseEvent


@dataclass
class GetRandomFlowerEvent(BaseEvent):
    event_title: ClassVar[str] = "Random Art Recieved Event"

    flower_name: str
    flower_path: str
