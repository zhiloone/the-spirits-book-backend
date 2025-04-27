from typing import Literal
from loguru import logger
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv(override=True)


class Settings(BaseSettings):
    ENVIRONMENT: Literal["development", "production"] = Field(default="development")

    DB_URI: str
    DB_NAME: str

    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


try:
    settings = Settings()
except ValidationError as e:
    logger.error("Environment variable validation failed!", e)
    raise
