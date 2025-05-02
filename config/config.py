# config/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Mantener compatibilidad con código existente
    MANGA_BASE_URL: str = os.environ.get("MANGA_BASE_URL", "https://zonatmo.com/")
    BASE_URL: str = MANGA_BASE_URL  # Alias para mantener compatibilidad

    API_BASE_URL: str = os.environ.get("API_BASE_URL", "http://localhost:8000")
    API_PREFIX: str = "/api/v1"

    @property
    def FULL_API_URL(self) -> str:
        return f"{self.API_BASE_URL}{self.API_PREFIX}"

    class Config:
        env_file = ".env"


settings = Settings()