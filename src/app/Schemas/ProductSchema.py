from pydantic import BaseModel,EmailStr

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    class Config:
        orm_mode = True