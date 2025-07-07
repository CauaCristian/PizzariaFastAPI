from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

db = create_engine(DATABASE_URL)
Base = declarative_base()

def init_session():
    session = sessionmaker(bind=db)
    return session()
