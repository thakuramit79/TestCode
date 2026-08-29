from functools import lru_cache
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "BookMyQ"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    postgres_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/bookmyq"
    redis_url: str = "redis://localhost:6379/0"
    rabbitmq_url: str = "amqp://guest:guest@localhost:5672/"
    elasticsearch_url: str = "http://localhost:9200"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60 * 24


@lru_cache
def get_settings() -> Settings:
    return Settings()
