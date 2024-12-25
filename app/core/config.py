from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Stocktober"
    database_url: str
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
