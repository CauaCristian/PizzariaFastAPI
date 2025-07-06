from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

db = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=db)

Base = declarative_base()
