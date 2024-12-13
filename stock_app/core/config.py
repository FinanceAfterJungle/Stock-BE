from pydantic_settings import BaseSettings, SettingsConfigDict

# from functools import lru_cache


class Settings(BaseSettings):
    ENV: str

    # MySQL 설정 정보
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


def get_setting():
    return Settings()
