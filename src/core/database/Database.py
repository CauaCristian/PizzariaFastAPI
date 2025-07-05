from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = os.getenv("DATABASE_URL")

db = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=db)

Base = declarative_base()
