from pydantic import BaseModel, ConfigDict

from enum import Enum

class StatusEnum(str, Enum):
    pedente = "PENDENTE"
    cancelado = "CANCELADO"
    finalizado = "FINALIZADO"

class OrderCreate(BaseModel):
    user_id: int

class OrderResponse(BaseModel):
    id: int
    status: StatusEnum
    price: float
    user_id: int
    model_config = ConfigDict(from_attributes=True)

