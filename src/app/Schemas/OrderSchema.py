from pydantic import BaseModel

from enum import Enum

class StatusEnum(str, Enum):
    pedente = "PEDENTE"
    cancelado = "CANCELADO"
    finalizado = "FINALIZADO"

class OrderCreate(BaseModel):
    user_id: int

class OrderResponse(BaseModel):
    id: int
    status: StatusEnum
    price: float
    user_id: int
    class Config:
        orm_mode = True

