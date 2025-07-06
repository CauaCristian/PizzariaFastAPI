from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

db = create_engine(DATABASE_URL)
Base = declarative_base()

def init_session():
    session = sessionmaker(bind=db)
    return session()
