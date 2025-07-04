from fastapi import APIRouter

ProductController = APIRouter()

@ProductController.get("/")
async def index():
    return {"message": "product Router"}

