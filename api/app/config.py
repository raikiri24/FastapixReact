from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Hobby Ballers API"

    log_level: str
    log_format: str

    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str
    mysql_charset: str

    redis_url: str
    redis_ssl: bool
    redis_host: str
    redis_port: str
    redis_db: int
    redis_password: str
    redis_decode_response: bool
    redis_cache_ttl: int
    redis_long_ttl: int

    database_uri: str

    class Config:
        env_file = ".env"


settings = Settings()
