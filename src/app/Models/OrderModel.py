
from sqlalchemy import Column, Integer, ForeignKey, String, Float

from src.core.database.Database import Base
class OrderModel(Base):
    __tablename__ = "order"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String, default="PENDING",nullable=False)
    price = Column("price",Float,nullable=False,default=0)
    user_id = Column("user_id",Integer, ForeignKey("user.id"),nullable=False)

    def __init__(self, status, user_id, price = 0):
        self.status = status
        self.user_id = user_id
        self.price = price