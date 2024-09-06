from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongo_db_connection_uri: str = Field(alias="MONGO_DB_CONNECTION_URI")
    mongo_db_admin_password: str = Field(alias="MONGO_DB_ADMIN_PASSWORD")
    mongo_db_admin_username: str = Field(default="postgres", alias="MONGO_DB_ADMIN_USERNAME")

    debug: bool = Field(default=True, alias="DEBUG")
