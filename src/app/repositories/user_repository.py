import os
import sys
from sqlalchemy.exc import SQLAlchemyError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app.models.user_model import UserModel
from src.core.database.database import DatabaseConfig

class UserRepository:

    def __init__(self):
        self.database_config = DatabaseConfig()
        self.session = self.database_config.init_session()

    def get_user_by_id(self,user_id: int):
        try:
            return self.session.query(UserModel).filter_by(id=user_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar usuário por ID: {e}")
        finally:
            self.session.close()

    def get_user_by_email(self,email: str):
        try :
            return self.session.query(UserModel).filter_by(email=email).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao buscar usuário por email: {e}")
        finally:
            self.session.close()

    def save_user(self,user: UserModel):
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao salvar usuário: {e}")
        finally:
            self.session.close()

    def update_user(self,user: UserModel):
        try:
            self.session.merge(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao atualizar usuário: {e}")
        finally:
            self.session.close()

    def delete_user(self,user: UserModel):
        try:
            self.session.delete(user)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise SQLAlchemyError(f"Erro ao deletar usuário: {e}")
        finally:
            self.session.close()