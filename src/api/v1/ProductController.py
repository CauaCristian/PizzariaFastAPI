from fastapi import APIRouter

ProductController = APIRouter()

@ProductController.get("/")
async def hello():
    return {"message": "product Router"}

