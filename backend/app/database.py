from sqlalchemy import create_engine #gives tool for connection between application and database
from sqlalchemy.orm import declarative_base #gives foundation for database models
from sqlalchemy.orm import sessionmaker
DATABASE_URL="sqlite:///./steelflow.db" #says our db is sqlite file called steelflow.db
engine=create_engine(DATABASE_URL) #creates database engine
Base=declarative_base() #creates base that future orm will inherit
SessionLocal=sessionmaker(bind=engine)
