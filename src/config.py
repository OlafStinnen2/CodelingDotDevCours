from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Tell Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env")

    # These fields have default empty strings and can be
    # overridden by values in the .env file.
    provider: str = ""
    api_key: str = ""
    oracle_model: str = ""

def get_settings() -> Settings:
    return Settings()
