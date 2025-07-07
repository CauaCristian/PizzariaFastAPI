from passlib.context import CryptContext

BcryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return BcryptContext.hash(password)
def verify_password(plain_password: str, hashed_password: str):
    return BcryptContext.verify(plain_password, hashed_password)