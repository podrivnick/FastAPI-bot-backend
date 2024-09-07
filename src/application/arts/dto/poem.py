from dataclasses import dataclass


@dataclass(frozen=True)
class DTOPoem:
    poem_title: str
    poem_author: str
    poem_text: str
    poem_date: str
