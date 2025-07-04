from fastapi import FastAPI
from src.api.v1.AuthController import AuthController
from src.api.v1.UserController import UserController
from src.api.v1.OrderController import OrderController
from src.api.v1.ProductController import ProductController
app = FastAPI()

app.include_router(AuthController,prefix="/api/v1/auth",tags=["auth"])
app.include_router(UserController,prefix="/api/v1/user",tags=["user"])
app.include_router(OrderController,prefix="/api/v1/order",tags=["order"])
app.include_router(ProductController,prefix="/api/v1/product",tags=["product"])

