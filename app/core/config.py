from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = 'Weather Playlist'

    CACHE_HOST: str
    CACHE_PORT: int
    CACHE_DB: int

    OPENWEATHER_API_KEY: str
    OPENWEATHER_UNITS: str


settings = Settings()
