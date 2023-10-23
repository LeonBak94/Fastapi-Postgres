import os
from dotenv import dotenv_values

ENV = dotenv_values(".env")


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = ENV["POSTGRES_USER"]
    POSTGRES_PASSWORD = ENV["POSTGRES_PASSWORD"]
    POSTGRES_SERVER: str = ENV["POSTGRES_SERVER"]
    POSTGRES_PORT: str = ENV["POSTGRES_PORT"]
    POSTGRES_DB: str = ENV["POSTGRES_DB"]
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = ENV["SECRET_KEY"]
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
