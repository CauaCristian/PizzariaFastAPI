from fastapi import APIRouter

UserController = APIRouter()

@UserController.get("/")
async def hello():
    return {"message": "user Router"}