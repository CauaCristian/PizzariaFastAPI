from fastapi import APIRouter

OrderController = APIRouter()

@OrderController.get("/")
async def hello():
    return {"message": "order Router"}