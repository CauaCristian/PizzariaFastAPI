import os
import sys



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.repositories.product_repository import ProductRepository
from src.app.schemas.product_schema import ProductCreate, ProductResponse
from src.core.security.token import Token


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.token = Token()

    def create_product(self, token:str ,product:ProductCreate):
        try:
            self.token.verify_token(token)
            self.token.verify_role_permission(token,"admin")
            from src.app.models.product_model import ProductModel
            new_product = ProductModel(name=product.name,description=product.description,size=product.size,price=product.price)
            new_product = self.product_repository.create_product(new_product)
            product_response = ProductResponse(
                id=new_product.id,
                name=new_product.name,
                description=new_product.description,
                size=new_product.size,
                price=new_product.price
            )
            return product_response
        except Exception as e:
            raise Exception(f"Erro ao criar produto: {e}") from e
