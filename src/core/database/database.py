from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class DatabaseConfig:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def init_session(self):
        return self.SessionLocal()
