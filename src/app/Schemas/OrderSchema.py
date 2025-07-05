from pydantic import BaseModel


class Order(BaseModel):
    status: str
    user_id: int

