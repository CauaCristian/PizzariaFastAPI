import os
import sys

from sqlalchemy.exc import SQLAlchemyError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.core.database.database import init_session
from src.app.models.order_model import OrderModel
class OrderRepository:
    def create_order(self, order: OrderModel):
        session = init_session()
        try:
            session.add(order)
            session.commit()
            session.refresh(order)
            return order
        except SQLAlchemyError as e:
            session.rollback()
            raise SQLAlchemyError(f"Erro na criação de pedido: {e}") from e
        finally:
            session.close()


    def get_order_by_id(self, order_id):
        session = init_session()
        try:
            order = session.query(OrderModel).filter_by(id=order_id).first()
            return order
        except SQLAlchemyError as e:
            session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar pedido: {e}") from e
        finally:
            session.close()

    def update_order(self, order):
        session = init_session()
        try:
            session.merge(order)
            session.commit()
            session.refresh(order)
            return order
        except SQLAlchemyError as e:
            session.rollback()
            raise SQLAlchemyError(f"Erro ao atualizar pedido: {e}") from e
        finally:
            session.close()

    def delete_order(self, order):
        session = init_session()
        try:
            session.delete(order)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise SQLAlchemyError(f"Erro ao deletar pedido: {e}") from e
        finally:
            session.close()