from dataclasses import dataclass

from src.domain.flowers.events.flowers import GetRandomFlowerEvent
from src.infrastructure.mediator.handlers.event import EventHandler
from src.infrastructure.message_broker.convertors import convert_event_to_broker_message


@dataclass
class GetRandomFlowerEventHandler(EventHandler[GetRandomFlowerEvent, None]):
    async def handle(self, event: GetRandomFlowerEvent) -> None:
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event),
            key=str(event.event_id).encode(),
        )
