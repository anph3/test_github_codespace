from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)

class Settings(BaseSettings):
    DEBUG: bool = True

settings = Settings()