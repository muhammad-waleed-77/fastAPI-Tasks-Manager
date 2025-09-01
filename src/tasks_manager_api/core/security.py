from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


# to create hashed password from plane one 
def get_password_hash(plane_password: str):
    return pwd_context.hash(plane_password)


# verify hash and plane pwd
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
