from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:1111@localhost:5432/contacts"
    SECRET_KEY_JWT: str = "secret_key"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: EmailStr = "postgres@mail.com"
    MAIL_PASSWORD: str = "postgres"
    MAIL_FROM: str = "postgres"
    MAIL_PORT: int = 567234
    MAIL_SERVER: str = "postgres"
    REDIS_DOMAIN: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    CLOUDINARY_NAME: str = 'dkynttk6x'
    CLOUDINARY_API_KEY: int = 293588615818463
    CLOUDINARY_API_SECRET: str = "a0pppMNrmEQkSD_MgXNY87c_i0rs"

    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "HS512"]:
            raise ValueError("algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8") 


config = Settings()
