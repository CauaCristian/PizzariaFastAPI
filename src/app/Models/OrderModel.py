import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import Column, Integer, ForeignKey, String, Float
from src.core.database.Database import Base

class OrderModel(Base):
    __tablename__ = "order"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String,nullable=False)
    price = Column("price",Float,nullable=False,default=0)
    user_id = Column("user_id",Integer, ForeignKey("user.id"),nullable=False)

    def __init__(self, user_id, status = "PENDENTE",  price = 0):
        self.status = status
        self.user_id = user_id
        self.price = price