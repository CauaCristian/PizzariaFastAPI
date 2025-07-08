import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.core.database.database import DatabaseConfig
from src.app.models.item_order_model import ItemOrderModel
class ItemOrderRepository:
    def __init__(self):
        self.db = DatabaseConfig()
        self.session = self.db.init_session()

    def create_item_order(self, item_order):
        self.session.add(item_order)
        self.session.commit()
        self.session.refresh(item_order)
        return item_order

    def get_item_order_by_id(self, item_order_id: int):
        return self.session.query(ItemOrderModel).filter(ItemOrderModel.id == item_order_id).first()

    def get_all_items_orders(self):
        return self.session.query(ItemOrderModel).all()

    def update_item_order(self, item_order):
        self.session.commit()
        return item_order

    def delete_item_order(self, item_order_id: int):
        item_order = self.get_item_order_by_id(item_order_id)
        if item_order:
            self.session.delete(item_order)
            self.session.commit()
            return True
        return False