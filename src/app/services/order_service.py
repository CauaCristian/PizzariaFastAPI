import os
import sys
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.models.order_model import OrderModel

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app.repositories.order_repository import OrderRepository
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.order_schema import OrderCreate, OrderResponse

userRepository = UserRepository()
orderRepository = OrderRepository()


class OrderService:

    def create_order(self, order_schema: OrderCreate):
        try:
            user = userRepository.get_user_by_id(order_schema.user_id)
            if user is None:
                raise HTTPException(status_code=400, detail="ID de usuário inválido ou não encontrado.")

            order = OrderModel(user_id=user.id)
            order = orderRepository.create_order(order)
            return OrderResponse.from_orm(order)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar pedido: {e}") from e

    def get_order_by_id(self, order_id):
        try:
            order = orderRepository.get_order_by_id(order_id)
            if order is None:
                raise HTTPException(status_code=404, detail="Pedido não encontrado.")
            return order
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar pedido: {e}") from e

    def update_order(self, order):
        try:
            return orderRepository.update_order(order)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar pedido: {e}") from e

    def delete_order(self, order_id):
        try:
            return orderRepository.delete_order(order_id)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao deletar pedido: {e}") from e
