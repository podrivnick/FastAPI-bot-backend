from dataclasses import dataclass
from typing import AsyncIterator

import orjson
from aiokafka import AIOKafkaConsumer
from aiokafka.producer import AIOKafkaProducer
from src.infrastructure.message_broker.base import BaseMessageBroker


@dataclass
class KafkaMessageBroker(BaseMessageBroker):
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    async def send_message(self, key: bytes, topic: str, value: dict):
        value_bytes = orjson.dumps(value)

        await self.producer.send(topic=topic, key=key, value=value_bytes)

    async def start_consuming(self, topic: str) -> AsyncIterator[dict]:
        self.consumer.subscribe(topics=[topic])

        async for message in self.consumer:
            yield orjson.loads(message.value)

    async def stop_consuming(self):
        self.consumer.unsubscribe()

    async def close(self):
        await self.consumer.stop()
        await self.producer.stop()

    async def start(self):
        await self.producer.start()
        await self.consumer.start()
