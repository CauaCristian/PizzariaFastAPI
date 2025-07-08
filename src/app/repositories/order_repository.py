import os
import sys
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.core.database.database import DatabaseConfig
from src.app.models.order_model import OrderModel

class OrderRepository:

    def __init__(self):
        self.database_config = DatabaseConfig()
        self.session = self.database_config.init_session()

    def get_order_by_id(self, order_id: int) -> Optional[OrderModel]:
        try:
            return self.session.query(OrderModel).filter(OrderModel.id == order_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar pedido por ID: {e}")
        finally:
            self.session.close()

    def get_order_by_user_id(self, user_id: int) -> List[OrderModel]:
        try:
            return self.session.query(OrderModel).filter(OrderModel.user_id == user_id).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar pedidos por usuário: {e}")
        finally:
            self.session.close()

    def get_order_by_user_id_and_status(self, user_id: int, status: str) -> List[OrderModel]:
        try:
            return self.session.query(OrderModel).filter(
                OrderModel.user_id == user_id,
                OrderModel.status == status
            ).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar pedidos por usuário e status: {e}")
        finally:
            self.session.close()

    def create_order(self, order: OrderModel) -> OrderModel:
        try:
            self.session.add(order)
            self.session.commit()
            self.session.refresh(order)
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao criar pedido: {e}")
        finally:
            self.session.close()

    def update_order(self, order: OrderModel) -> OrderModel:
        try:
            self.session.merge(order)
            self.session.commit()
            self.session.refresh(order)
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao atualizar pedido: {e}")
        finally:
            self.session.close()

    def delete_order(self, order: OrderModel) -> None:
        try:
            self.session.delete(order)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao deletar pedido: {e}")
        finally:
            self.session.close()
