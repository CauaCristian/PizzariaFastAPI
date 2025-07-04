from fastapi import APIRouter

AuthController = APIRouter()

@AuthController.get("/")
async def hello():
    return {"message": "auth Router"}