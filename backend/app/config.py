from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url:str="sqlite:///./steelflow.db"

settings=Settings()