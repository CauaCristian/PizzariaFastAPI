import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.models.product_model import ProductModel
from src.core.database.database import DatabaseConfig
class ProductRepository:
    def __init__(self):
        self.db = DatabaseConfig()
        self.session = self.db.init_session()

    def create_product(self, product: ProductModel):
        try:
            self.session.add(product)
            self.session.commit()
            self.session.refresh(product)
            return product
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Erro ao criar produto: {e}")
        finally:
            self.session.close()
    def get_product_by_id(self, product_id: int) -> ProductModel:
        try:
            return self.session.query(ProductModel).filter(ProductModel.id == product_id).first()
        except Exception as e:
            raise Exception(f"Erro ao buscar produto por ID: {e}")
        finally:
            self.session.close()
    def get_all_products(self) -> list[ProductModel]:
        try:
            return self.session.query(ProductModel).all()
        except Exception as e:
            raise Exception(f"Erro ao buscar todos os produtos: {e}")
        finally:
            self.session.close()
    def update_product(self, product: ProductModel) -> ProductModel:
        try:
            self.session.merge(product)
            self.session.commit()
            self.session.refresh(product)
            return product
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Erro ao atualizar produto: {e}")
        finally:
            self.session.close()
    def delete_product(self, product_id: int) -> None:
        try:
            product = self.get_product_by_id(product_id)
            if product:
                self.session.delete(product)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Erro ao deletar produto: {e}")
        finally:
            self.session.close()