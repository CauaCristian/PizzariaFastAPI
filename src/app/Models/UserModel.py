from sqlalchemy import Column, Integer, String
from src.core.database.Database import Base

class User(Base):

    __tablename__ = "user"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("name",String,nullable=False)
    email = Column("email",String,nullable=False)
    password = Column("password",String,nullable=False)
    role = Column("role",String,default="user")

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role