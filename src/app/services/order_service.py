import os
import sys
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from src.app.models.order_model import OrderModel
from src.app.repositories.item_order_repository import ItemOrderRepository
from src.app.repositories.product_repository import ProductRepository
from src.core.security.token import Token
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.repositories.order_repository import OrderRepository
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.order_schema import OrderCreate, OrderResponse, ItemOrderResponse

class OrderService:

    def __init__(self):
        self.order_repository = OrderRepository()
        self.user_repository = UserRepository()
        self.item_order_repository = ItemOrderRepository()
        self.product_repository = ProductRepository()
        self.token = Token()

    def create_order(self, order_schema: OrderCreate, token: str) :
        try:
            payload = self.token.verify_token(token)
            self.token.verify_user_permission(payload["user_id"], order_schema.user_id)
            user = self.user_repository.get_user_by_id(order_schema.user_id)
            if user is None:
                raise HTTPException(status_code=400, detail="ID de usuário inválido ou não encontrado.")
            for item in order_schema.itemsOrder:
                product = self.product_repository.get_product_by_id(item.product_id)
                if product is None:
                    raise HTTPException(status_code=400, detail=f"Produto com ID {item.product_id} não encontrado.")
            order = OrderModel(user_id=user.id)
            order = self.order_repository.create_order(order)
            price = 0
            items_order : list[ItemOrderResponse] = []
            for item in order_schema.itemsOrder:
                price += self.product_repository.get_product_by_id(item.product_id).price * item.quantity
            for item in order_schema.itemsOrder:
                item = ItemOrderResponse(
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price= self.product_repository.get_product_by_id(item.product_id).price * item.quantity
                )
                items_order.append(item)
            order_response = OrderResponse(
                id=order.id,
                status=order.status,
                price=price,
                user_id=order.user_id,
                itemsOrder=items_order,
            )
            return order_response
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar pedido: {e}") from e

    def get_order_by_user_id(self, user_id: int, token: str) -> list[OrderModel]:
        try:
            payload = self.token.verify_token(token)
            self.token.verify_user_permission(payload["user_id"], user_id)
            order = self.order_repository.get_order_by_user_id(user_id)
            if order is None:
                raise HTTPException(status_code=404, detail="Pedido não encontrado.")
            return order
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar pedido: {e}") from e

    def get_order_by_user_id_and_status(self, user_id: int, status: str, token: str):
        try:
            payload = self.token.verify_token(token)
            self.token.verify_user_permission(payload["user_id"], user_id)
            order = self.order_repository.get_order_by_user_id_and_status(user_id, status)
            if order is None:
                raise HTTPException(status_code=404, detail="Pedido não encontrado.")
            return order
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar pedido: {e}") from e

    def update_status_order(self, order_id: int, status: str, token: str):
        try:
            self.token.verify_token(token)
            self.token.verify_role_permission(token, "admin")
            order = self.order_repository.get_order_by_id(order_id)
            if order is None:
                raise HTTPException(status_code=404, detail="Pedido não encontrado.")
            order.status = status
            updated_order = self.order_repository.update_order(order)
            return OrderResponse.from_orm(updated_order)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar pedido: {e}") from e