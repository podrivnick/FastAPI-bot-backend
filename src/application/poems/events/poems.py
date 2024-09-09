from dataclasses import dataclass

from src.domain.poems.events.poems import GetRandomPoemEvent
from src.infrastructure.mediator.handlers.event import EventHandler
from src.infrastructure.message_broker.convertors import convert_event_to_broker_message


@dataclass
class GetRandomPoemEventHandler(EventHandler[GetRandomPoemEvent, None]):
    async def handle(self, event: GetRandomPoemEvent) -> None:
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event),
            key=str(event.event_id).encode(),
        )
