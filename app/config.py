from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"

    SENDGRID_API_KEY: str
    SENDGRID_SENDER_EMAIL: EmailStr


config = Config()
