from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, Field
from pydantic import EmailStr


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]  # go 3 levels up from config.py

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = str(BASE_DIR / ".env"),
        env_ignore_empty=True,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str



settings = Settings()


