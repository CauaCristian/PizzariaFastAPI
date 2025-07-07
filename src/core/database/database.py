from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

Base = declarative_base()

class DatabaseConfig:

    def __init__(self):
        load_dotenv()
        self.database_url = os.getenv("DATABASE_URL")
        self.db = create_engine(self.database_url)
        self.session = sessionmaker(bind=self.db)

    def init_session(self):
        return self.session()
