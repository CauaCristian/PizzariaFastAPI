import os
import sys
from sqlalchemy.exc import SQLAlchemyError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.core.database.database import DatabaseConfig
from src.app.models.order_model import OrderModel

class OrderRepository:

    def __init__(self):
        self.database_config = DatabaseConfig()
        self.session = self.database_config.init_session()

    def create_order(self, order: OrderModel):
        try:
            self.session.add(order)
            self.session.commit()
            self.session.refresh(order)
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro na criação de pedido: {e}") from e
        finally:
            self.session.close()

    def get_order_by_id(self, order_id):
        try:
            order = self.session.query(OrderModel).filter_by(id=order_id).first()
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar pedido: {e}") from e
        finally:
            self.session.close()

    def update_order(self, order):
        try:
            self.session.merge(order)
            self.session.commit()
            self.session.refresh(order)
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao atualizar pedido: {e}") from e
        finally:
            self.session.close()

    def delete_order(self, order):
        try:
            self.session.delete(order)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao deletar pedido: {e}") from e
        finally:
            self.session.close()