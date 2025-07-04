from fastapi import APIRouter

AuthController = APIRouter()

@AuthController.get("/")
async def index():
    return {"message": "auth Router"}