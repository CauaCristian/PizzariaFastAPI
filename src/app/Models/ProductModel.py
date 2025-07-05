from sqlalchemy import Column, Integer, String, Float
from src.core.database.Database import Base
from sqlalchemy_utils import ChoiceType

class ProductModel(Base):
    __tablename__ = "product"

    PRODUCT_SIZE = (
        ("P", "P"),
        ("M", "M"),
        ("G", "G"),
    )

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    name = Column("name",String,nullable=False)
    description = Column("description",String,nullable=False)
    size = Column("size",ChoiceType(choices=PRODUCT_SIZE),nullable=False)
    price = Column("price",Float,nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
