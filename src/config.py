import pathlib

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: str

    DB_HOST: str
    DB_PORT: str
    DB_PASS: str
    DB_NAME: str
    DB_USER: str

    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


load_dotenv(find_dotenv(".env"))
settings = Settings()

if settings.MODE == "TEST":
    directory = pathlib.Path.cwd() / "tests/fixtures/test_xml_files"
else:
    directory = pathlib.Path.cwd() / "xml_files"

SITE_URL = "https://..."
