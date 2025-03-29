from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DATABASE_URL: str
    APP_NAME: str = "main_api"

    class Config:
        env_file = ".env"

settings = Settings()