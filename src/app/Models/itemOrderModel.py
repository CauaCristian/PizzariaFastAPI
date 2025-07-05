from sqlalchemy import Column, Integer, ForeignKey

from src.core.database.Database import Base
class ItemOrderModel(Base):
    __tablename__ = "item_order"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    order_id = Column("order_id",Integer,ForeignKey('order.id'),nullable=False)
    product_id = Column("product_id",Integer,ForeignKey('product.id'),nullable=False)

    def __init__(self, order_id, product_id):
        self.order_id = order_id
        self.product_id = product_id