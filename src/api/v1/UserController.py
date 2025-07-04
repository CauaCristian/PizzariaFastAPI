from fastapi import APIRouter

UserController = APIRouter()

@UserController.get("/")
async def index():
    return {"message": "user Router"}