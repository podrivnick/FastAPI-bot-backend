import logging

import orjson
from src.domain.common.events.base import BaseEvent


def convert_event_to_broker_message(event: BaseEvent) -> bytes:
    logging.info(f"Код дошел до orjson {event}")
    return orjson.dumps(event)
