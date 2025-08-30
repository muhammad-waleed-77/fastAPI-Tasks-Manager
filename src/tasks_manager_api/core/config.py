from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, Field




class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = "../../../.env", 
        env_ignore_empty=True,
        env_file_encoding="utf-8",
        extra="ignore",
        )

    API_V1_STR: str = "/api/v1"

    DATABASE_URL: PostgresDsn



settings = Settings()


