from pydantic import BaseModel

from src.app.Schemas.OrderSchema import StatusEnum


class ItemOrderCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int

class ItemOrderUpdate(BaseModel):
    product_id: int
    quantity: int

class ItemOrderResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price: float
    class Config:
        orm_mode = True