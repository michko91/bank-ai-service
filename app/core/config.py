import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bank AI Service"
    PROJECT_VERSION: str = "1.0.0"
    # Standartwert 10000, falls nichts in der env. steht
    LOAN_MAX_LIMIT: float = float(os.getenv("LOAN_MAX_LIMIT", 10000.0))

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Hier kommen später die AI-Keys rein
    # OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

# Singleton-Instanz der Settings
settings = Settings()