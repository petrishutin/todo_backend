from pydantic import BaseSettings


class Settings(BaseSettings):
    """Server config settings"""

    # Mongo Engine settings
    MONGO_URI: str = "mongodb://test:test@localhost:27117"
    FILE_STORAGE_URL: str = "http://localhost:8001"

    # Security settings
    AUTHJWT_SECRET_KEY: str = "secret"
    SALT: str = "$2b$12$GeBAcXwm5tCsWVf2992qdO"


def get_settings() -> Settings:
    """Get server config settings"""
    return Settings()