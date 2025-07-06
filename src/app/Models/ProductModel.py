import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import Column, Integer, String, Float
from src.core.database.Database import Base

class ProductModel(Base):
    __tablename__ = "product"


    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("name",String,nullable=False)
    description = Column("description",String,nullable=False)
    size = Column("size",String,nullable=False)
    price = Column("price",Float,nullable=False)

    def __init__(self, name, description,size, price):
        self.name = name
        self.description = description
        self.size = size
        self.price = price
