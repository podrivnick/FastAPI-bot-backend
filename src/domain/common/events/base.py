from abc import ABC
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from typing import ClassVar
from uuid import UUID

from uuid6 import uuid7


@dataclass
class BaseEvent(ABC):
    title: ClassVar[str]

    event_id: UUID = field(init=False, kw_only=True, default_factory=uuid7)
    event_timestamp: datetime = field(
        init=False,
        kw_only=True,
        default_factory=datetime.utcnow,
    )
