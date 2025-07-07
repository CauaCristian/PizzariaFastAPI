import os
import sys
from sqlalchemy.exc import SQLAlchemyError
from src.app.schemas.auth_schema import AuthLogin, AuthResponse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.core.security.bcrypt import Bcrypt
from fastapi import HTTPException
from src.app.models.user_model import UserModel
from src.app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from src.app.repositories.user_repository import UserRepository
from src.core.security.token import Token
class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()
        self.bcrypt = Bcrypt()
        self.token = Token()

    def create_user(self,user_schema: UserCreate):
        try:
            if self.user_repository.get_user_by_email(user_schema.email):
                raise HTTPException(status_code=400, detail="Email já está em uso.")

            if len(user_schema.password) < 6:
                raise HTTPException(status_code=400, detail="Senha muito curta. Use pelo menos 6 caracteres.")

            user = UserModel(
                name=user_schema.name,
                email=user_schema.email,
                password= self.bcrypt.hash(user_schema.password),
            )
            user = self.user_repository.save_user(user)
            return UserResponse.from_orm(user)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Erro ao criar usuário.") from e

    def login_user(self,auth_login: AuthLogin):
        try:
            user = self.user_repository.get_user_by_email(auth_login.email)
            if not user:
                raise HTTPException(status_code=400, detail="Usuário não encontrado.")
            if not self.bcrypt.verify(auth_login.password,user.password):
                raise HTTPException(status_code=400, detail="Senha incorreta.")
            auth_response = AuthResponse(access_token=self.token.generate_token(user.id, user.role),refresh_token= self.token.generate_refresh_token(user.id))
            return auth_response
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Erro ao buscar usuário.") from e

    def refresh_token(self, refresh_token: str):
        try:
            dict = self.token.verify_token(refresh_token)
            if not dict:
                raise HTTPException(status_code=400, detail="Token inválido ou expirado.")
            user = self.user_repository.get_user_by_id(dict["user_id"])
            new_access_token = self.token.generate_token(user.id, user.role)
            new_refresh_token = self.token.generate_refresh_token(user.id)
            return AuthResponse(access_token=new_access_token, refresh_token=new_refresh_token)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail) from e