import os
import sys

from sqlalchemy.exc import SQLAlchemyError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.security.Bcrypt import hash_password,verify_password
from fastapi import HTTPException
from src.app.repositories import UserRepository
from src.app.models.UserModel import UserModel
from src.app.schemas import UserSchema

def create_user(user_schema: UserSchema.UserCreate):
    try:
        if UserRepository.get_user_by_email(user_schema.email):
            raise HTTPException(status_code=400, detail="Email já está em uso.")

        if len(user_schema.password) < 6:
            raise HTTPException(status_code=400, detail="Senha muito curta. Use pelo menos 6 caracteres.")

        user = UserModel(
            name=user_schema.name,
            email=user_schema.email,
            password= hash_password(user_schema.password),
        )
        user = UserRepository.save_user(user)
        return UserSchema.UserResponse.from_orm(user)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário.") from e
