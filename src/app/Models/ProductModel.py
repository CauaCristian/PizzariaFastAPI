from sqlalchemy import Column, Integer, String, Float

from src.core.database.Database import Base
class ProductModel(Base):
    __tablename__ = "product"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("name",String,nullable=False)
    description = Column("description",String,nullable=False)
    price = Column("price",Float,nullable=False)
    quantity = Column("quantity",Integer,nullable=False)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
