from pydantic import BaseModel, ConfigDict


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
    model_config = ConfigDict(from_attributes=True)