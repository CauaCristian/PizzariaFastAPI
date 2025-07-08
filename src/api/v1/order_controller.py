from fastapi import APIRouter , Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.schemas.order_schema import OrderCreate, OrderResponse
from src.app.services.order_service import OrderService

OrderController = APIRouter()
orderService = OrderService()
security = HTTPBearer()

@OrderController.post("/create",response_model=OrderResponse,status_code=200)
async def create_order(order: OrderCreate, credentials: HTTPAuthorizationCredentials = Depends(security),response_model=OrderResponse):
    return orderService.create_order(order, credentials.credentials)