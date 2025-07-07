from fastapi import HTTPException

from dotenv import load_dotenv
import os
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

class Token:

    def __init__(self):
        load_dotenv()
        self.algorithm = os.getenv("ALGORITHM")
        self.secret_key = os.getenv("SECRET_KEY")
        self.expiration_time = int(os.getenv("TOKEN_EXPIRATION_TIME"))

    def generate_token(self,user_id: int,role: str):
        try:
            token = jwt.encode({
                "user_id": user_id,
                "role": role,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=self.expiration_time)
            }, self.secret_key, algorithm=self.algorithm)
            return token
        except JWTError as e:
            raise HTTPException(status_code=400, detail=f"Erro ao gerar token: {e}") from e

    def generate_refresh_token(self, user_id: int):
        try:
            token = jwt.encode({
                "user_id": user_id,
                "exp": datetime.now(timezone.utc) + timedelta(days=7)
            }, self.secret_key, algorithm=self.algorithm)
            return token
        except JWTError as e:
            raise HTTPException(status_code=400, detail=f"Erro ao gerar refresh token: {e}") from e

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError as e:
            raise HTTPException(status_code=400, detail=f"Token inválido ou expirado: {e}") from e