from sqlalchemy import create_engine #gives tool for connection between application and database
from sqlalchemy.orm import declarative_base #gives foundation for database models
from sqlalchemy.orm import sessionmaker
from .config import settings
DATABASE_URL=settings.database_url  #now if we change our congiguration to posstgresql we dont have to change datbase setup
engine=create_engine(DATABASE_URL) #creates database engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base=declarative_base() #creates base that future orm will inherit
