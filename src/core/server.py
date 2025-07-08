import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from src.api.v1.auth_controller import AuthController
from src.api.v1.user_controller import UserController
from src.api.v1.order_controller import OrderController
from src.api.v1.product_controller import ProductController
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST","PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(AuthController,prefix="/api/v1/auth",tags=["auth"])
app.include_router(UserController,prefix="/api/v1/user",tags=["user"])
app.include_router(OrderController,prefix="/api/v1/order",tags=["order"])
app.include_router(ProductController,prefix="/api/v1/product",tags=["product"])
