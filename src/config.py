from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    api_key: str = ""
    oracle_model: str = ""


def get_settings() -> Settings:
    return Settings()
