from pydantic import BaseModel, ConfigDict
from enum import Enum

class ItemOrderCreate(BaseModel):
    product_id: int
    quantity: int

class ItemOrderResponse(BaseModel):
    product_id: int
    quantity: int
    price: float

class StatusEnum(str, Enum):
    pedente = "PENDENTE"
    cancelado = "CANCELADO"
    finalizado = "FINALIZADO"

class OrderCreate(BaseModel):
    user_id: int
    itemsOrder: list[ItemOrderCreate]

class OrderResponse(BaseModel):
    id: int
    status: StatusEnum
    price: float
    user_id: int
    itemsOrder: list[ItemOrderResponse]


