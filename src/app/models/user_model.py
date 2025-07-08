import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import Column, Integer, String, Boolean
from src.core.database.database import Base

class UserModel(Base):

    __tablename__ = "user"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("name",String,nullable=False)
    email = Column("email",String,nullable=False,unique=True)
    password = Column("password",String,nullable=False)
    role = Column("role",String,default="user",nullable=False)

    def __init__(self, name, email, password, role="user"):
        self.name = name
        self.email = email
        self.password = password
        self.role = role