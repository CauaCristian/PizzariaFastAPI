from sqlalchemy import Column, Integer, ForeignKey, Float

from src.core.database.Database import Base
class ItemOrderModel(Base):

    __tablename__ = "items_order"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    order_id = Column("order_id",Integer,ForeignKey('order.id'),nullable=False)
    product_id = Column("product_id",Integer,ForeignKey('product.id'),nullable=False)
    quantity = Column("quantity",Integer,nullable=False)
    price = Column("price",Float,nullable=False)

    def __init__(self, order_id, product_id,quantity,price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price