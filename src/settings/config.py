from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongo_db_connection_uri: str = Field(alias="MONGO_DB_CONNECTION_URI")
    mongo_db_admin_password: str = Field(alias="MONGO_DB_ADMIN_PASSWORD")
    mongo_db_admin_username: str = Field(
        default="admin",
        alias="MONGO_DB_ADMIN_USERNAME",
    )
    mongodb_galery_database: str = Field(
        default="galery",
        alias="MONGODB_GALERY_DATABASE",
    )
    mongodb_arts_collection: str = Field(
        default="arts",
        alias="MONGODB_ARTS_COLLECTION",
    )
    mongodb_flowers_collection: str = Field(
        default="flowers",
        alias="MONGODB_FLOWERS_COLLECTION",
    )

    debug: bool = Field(default=True, alias="DEBUG")
