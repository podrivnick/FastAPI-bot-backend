from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    postgres_db: str = Field(alias='POSTGRES_DB')
    postgres_password: str = Field(alias='POSTGRES_PASSWORD')
    postgres_user: str = Field(default='postgres', alias='POSTGRES_USER')
    postgres_host: str = Field(default='postgres', alias='POSTGRES_HOST')
    postgres_port: int = Field(default=5432, alias='POSTGRES_PORT')

    debug: bool = Field(default=True, alias='DEBUG')
