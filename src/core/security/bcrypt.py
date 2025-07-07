from passlib.context import CryptContext

BcryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Bcrypt:
    def __init__(self):
        self.context = BcryptContext

    def hash(self, password: str) -> str:
        return self.context.hash(password)

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return self.context.verify(plain_password, hashed_password)
