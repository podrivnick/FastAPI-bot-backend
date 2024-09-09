from dataclasses import dataclass
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.poems import value_objects as vo
from src.domain.poems.events.poems import GetRandomPoemEvent


@dataclass
class Poem(AggregateRoot):
    poem_title: vo.PoemTitle
    poem_author: vo.PoemAuthor
    poem_text: vo.PoemText
    poem_date: vo.PoemDate

    @classmethod
    def create_poem(
        cls,
        poem_title: vo.PoemTitle,
        poem_author: vo.PoemAuthor,
        poem_text: vo.PoemText,
        poem_date: vo.PoemDate,
    ) -> Self:
        poem = cls(
            poem_title=poem_title,
            poem_author=poem_author,
            poem_text=poem_text,
            poem_date=poem_date,
        )

        poem.record_event(
            GetRandomPoemEvent(
                poem_title=poem.poem_title.to_raw(),
                poem_author=poem.poem_author.to_raw(),
                poem_text=poem.poem_text.to_raw(),
                poem_date=poem.poem_date.to_raw(),
            ),
        )

        return poem
