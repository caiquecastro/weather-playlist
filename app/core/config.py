from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = 'Weather Playlist'

    REDIS_URL: str

    OPENWEATHER_API_KEY: str
    OPENWEATHER_UNITS: str

    SENTRY_DSN: str


settings = Settings()
