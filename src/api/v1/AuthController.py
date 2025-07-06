from fastapi import APIRouter
from src.app.Schemas.UserSchema import UserCreate, UserResponse
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.Services import AuthService

AuthController = APIRouter()

@AuthController.get("/")
async def hello():
    return {"message": "auth Router"}

@AuthController.post("/singup",response_model=UserResponse,status_code=201)
async def create_user(user: UserCreate):
    return AuthService.create_user(user)