import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import APIRouter

UserController = APIRouter()

@UserController.get("/")
async def hello():
    return {"message": "user Router"}