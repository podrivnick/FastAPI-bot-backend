from abc import ABC
from dataclasses import dataclass
from typing import List

from motor.core import AgnosticClient


@dataclass
class BaseMongoDBRepository(ABC):
    mongo_db_client: AgnosticClient
    mongo_db_db_name: str
    mongo_db_collection: str

    @property
    def _collection(self) -> str:
        return self.mongo_db_client[self.mongo_db_db_name][self.mongo_db_collection]


saved_arts = [
    {
        "_id": "1",
        "art_name": "Jupiter",
        "art_direction": "modern",
        "art": "../fg/Jupiter",
        "art_description": "Some Description",
    },
    {
        "_id": "2",
        "art_name": "surrealism",
        "art_direction": "impressionist",
        "art": "../fg/Starry_Night",
        "art_description": "A masterpiece by Van Gogh",
    },
    {
        "_id": "3",
        "art_name": "Marilyn Monroe",
        "art_direction": "modern",
        "art": "../fg/Marilyn_Monroe",
        "art_description": "Famous pop art portrait by Andy Warhol",
    },
    {
        "_id": "4",
        "art_name": "The Persistence of Memory",
        "art_direction": "surrealism",
        "art": "../fg/The_Persistence_of_Memory",
        "art_description": "A surreal painting by Salvador Dalí",
    },
    {
        "_id": "5",
        "art_name": "The Great Wave off Kanagawa",
        "art_direction": "ukiyo-e",
        "art": "../fg/The_Great_Wave",
        "art_description": "Iconic Japanese woodblock print by Hokusai",
    },
    {
        "_id": "6",
        "art_name": "Composition VIII",
        "art_direction": "abstract",
        "art": "../fg/Composition_VIII",
        "art_description": "Abstract geometric composition by Wassily Kandinsky",
    },
]

saved_poems = [
    {
        "_id": "1",
        "poem_title": "Onegin",
        "poem_author": "Pushkin",
        "poem_text": "Some Text about Onegin",
        "poem_date": "06.06.2000",
    },
    {
        "_id": "2",
        "poem_title": "The Battle of Britain",
        "poem_author": "Winston Churchill",
        "poem_text": "Never in the field of human conflict was so much owed by so many to so few.",
        "poem_date": "20.05.1940",
    },
    {
        "_id": "3",
        "poem_title": "1984",
        "poem_author": "George Orwell",
        "poem_text": "It was a bright cold day in April, and the clocks were striking thirteen.",
        "poem_date": "08.06.1949",
    },
    {
        "_id": "4",
        "poem_title": "The Road Not Taken",
        "poem_author": "Robert Frost",
        "poem_text": "Two roads diverged in a yellow wood, and sorry I could not travel both.",
        "poem_date": "01.01.1916",
    },
    {
        "_id": "5",
        "poem_title": "Still I Rise",
        "poem_author": "Maya Angelou",
        "poem_text": "You may write me down in history with your bitter, twisted lies.",
        "poem_date": "21.10.1978",
    },
]

saved_flowers = [
    {
        "_id": "1",
        "flower_name": "Rose",
        "flower_path": "../flowers/Rose",
    },
    {
        "_id": "2",
        "flower_name": "Lily",
        "flower_path": "../flowers/Lily",
    },
    {
        "_id": "3",
        "flower_name": "Sunflower",
        "flower_path": "../flowers/Sunflower",
    },
    {
        "_id": "4",
        "flower_name": "Tulip",
        "flower_path": "../flowers/Tulip",
    },
    {
        "_id": "5",
        "flower_name": "Daisy",
        "flower_path": "../flowers/Daisy",
    },
    {
        "_id": "6",
        "flower_name": "Orchid",
        "flower_path": "../flowers/Orchid",
    },
]


def get_saved_arts() -> List[dict]:
    return [
        {
            "_id": "1",
            "art_name": "Jupiter",
            "art_direction": "modern",
            "art": "../fg/Jupiter",
            "art_description": "Some Description",
        },
        {
            "_id": "2",
            "art_name": "surrealism",
            "art_direction": "impressionist",
            "art": "../fg/Starry_Night",
            "art_description": "A masterpiece by Van Gogh",
        },
        {
            "_id": "3",
            "art_name": "Marilyn Monroe",
            "art_direction": "modern",
            "art": "../fg/Marilyn_Monroe",
            "art_description": "Famous pop art portrait by Andy Warhol",
        },
        {
            "_id": "4",
            "art_name": "The Persistence of Memory",
            "art_direction": "surrealism",
            "art": "../fg/The_Persistence_of_Memory",
            "art_description": "A surreal painting by Salvador Dalí",
        },
        {
            "_id": "5",
            "art_name": "The Great Wave off Kanagawa",
            "art_direction": "ukiyo-e",
            "art": "../fg/The_Great_Wave",
            "art_description": "Iconic Japanese woodblock print by Hokusai",
        },
        {
            "_id": "6",
            "art_name": "Composition VIII",
            "art_direction": "abstract",
            "art": "../fg/Composition_VIII",
            "art_description": "Abstract geometric composition by Wassily Kandinsky",
        },
    ]


def get_saved_poems() -> List[dict]:
    return [
        {
            "_id": "1",
            "poem_title": "Onegin",
            "poem_author": "Pushkin",
            "poem_text": "Some Text about Onegin",
            "poem_date": "06.06.2000",
        },
        {
            "_id": "2",
            "poem_title": "The Battle of Britain",
            "poem_author": "Winston Churchill",
            "poem_text": "Never in the field of human conflict was so much owed by so many to so few.",
            "poem_date": "20.05.1940",
        },
        {
            "_id": "3",
            "poem_title": "1984",
            "poem_author": "George Orwell",
            "poem_text": "It was a bright cold day in April, and the clocks were striking thirteen.",
            "poem_date": "08.06.1949",
        },
        {
            "_id": "4",
            "poem_title": "The Road Not Taken",
            "poem_author": "Robert Frost",
            "poem_text": "Two roads diverged in a yellow wood, and sorry I could not travel both.",
            "poem_date": "01.01.1916",
        },
        {
            "_id": "5",
            "poem_title": "Still I Rise",
            "poem_author": "Maya Angelou",
            "poem_text": "You may write me down in history with your bitter, twisted lies.",
            "poem_date": "21.10.1978",
        },
    ]


def get_saved_flowers() -> List[dict]:
    return [
        {
            "_id": "1",
            "flower_name": "Rose",
            "flower_path": "../flowers/Rose",
        },
        {
            "_id": "2",
            "flower_name": "Lily",
            "flower_path": "../flowers/Lily",
        },
        {
            "_id": "3",
            "flower_name": "Sunflower",
            "flower_path": "../flowers/Sunflower",
        },
        {
            "_id": "4",
            "flower_name": "Tulip",
            "flower_path": "../flowers/Tulip",
        },
        {
            "_id": "5",
            "flower_name": "Daisy",
            "flower_path": "../flowers/Daisy",
        },
        {
            "_id": "6",
            "flower_name": "Orchid",
            "flower_path": "../flowers/Orchid",
        },
    ]
