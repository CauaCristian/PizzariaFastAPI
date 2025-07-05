from pydantic import BaseModel

from enum import Enum

class SizeEnum(str, Enum):
    P = "P"
    M = "M"
    G = "G"

class ProductCreate(BaseModel):
    name: str
    description: str
    size: SizeEnum
    price: float


class ProductUpdate(BaseModel):
    name: str
    description: str
    size: SizeEnum
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    size: SizeEnum
    price: float
    class Config:
        orm_mode = True