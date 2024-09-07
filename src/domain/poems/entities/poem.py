from dataclasses import dataclass
from typing import Self

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.poems import value_objects as vo


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

        return poem
