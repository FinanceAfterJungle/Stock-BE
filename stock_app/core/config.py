from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # MySQL 설정 정보
    # MYSQL_HOST: str
    # MYSQL_PORT: int
    # MYSQL_ROOT_PASSWORD: str
    # MYSQL_DATABASE: str
    # MYSQL_USER: str
    # MYSQL_PASSWORD: str
    DATABASE_FILE: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


def get_setting():
    return Settings()
