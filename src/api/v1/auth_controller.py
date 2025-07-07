from fastapi import APIRouter
from src.app.schemas.user_schema import UserCreate, UserResponse
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.services.auth_service import AuthService
from src.app.schemas.auth_schema import AuthLogin, AuthResponse

AuthController = APIRouter()

authService = AuthService()

@AuthController.get("/")
async def hello():
    return {"message": "auth Router"}

@AuthController.post("/signup",response_model=UserResponse,status_code=200)
async def create_user(user: UserCreate):
    return authService.create_user(user)

@AuthController.post("/signin",response_model=AuthResponse,status_code=200)
async def login_user(auth_login: AuthLogin):
    return authService.login_user(auth_login)