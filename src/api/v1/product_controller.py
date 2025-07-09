from fastapi import APIRouter, Depends

ProductController = APIRouter()

from src.app.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse

from src.app.services.product_service import ProductService

product_service = ProductService()

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

@ProductController.get("/")
async def hello():
    return {"message": "product Router"}

@ProductController.post("/create",response_model=ProductResponse, status_code=200)
async def create_product(product: ProductCreate, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    return product_service.create_product(credentials.credentials, product)

