from fastapi import APIRouter

OrderController = APIRouter()

@OrderController.get("/")
async def index():
    return {"message": "order Router"}