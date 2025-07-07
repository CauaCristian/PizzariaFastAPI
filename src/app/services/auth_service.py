import os
import sys

from sqlalchemy.exc import SQLAlchemyError

from src.app.schemas.auth_schema import AuthLogin, AuthResponse
from src.app.services.order_service import userRepository

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.security.bcrypt import Bcrypt
from fastapi import HTTPException
from src.app.models.user_model import UserModel
from src.app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from src.app.repositories.user_repository import UserRepository

userRepository = UserRepository()
bcrypt = Bcrypt()

class AuthService:
    def create_user(self,user_schema: UserCreate):
        try:
            if userRepository.get_user_by_email(user_schema.email):
                raise HTTPException(status_code=400, detail="Email já está em uso.")

            if len(user_schema.password) < 6:
                raise HTTPException(status_code=400, detail="Senha muito curta. Use pelo menos 6 caracteres.")

            user = UserModel(
                name=user_schema.name,
                email=user_schema.email,
                password= bcrypt.hash(user_schema.password),
            )
            user = userRepository.save_user(user)
            return UserResponse.from_orm(user)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Erro ao criar usuário.") from e

    def login_user(self,auth_login: AuthLogin):
        try:
            user = userRepository.get_user_by_email(auth_login.email)
            if not user:
                raise HTTPException(status_code=400, detail="Usuário não encontrado.")
            if not bcrypt.verify(auth_login.password,user.password):
                raise HTTPException(status_code=400, detail="Senha incorreta.")
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Erro ao buscar usuário.") from e
        auth_response = AuthResponse(access_token="seu_token_aqui")
        return auth_response
