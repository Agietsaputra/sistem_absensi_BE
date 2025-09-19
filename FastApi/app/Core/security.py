from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: int = None) -> str:
    expire = datetime.utcnow() + timedelta(minutes=(expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"sub": str(subject), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: int = None) -> str:
    expire = datetime.utcnow() + timedelta(minutes=(expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"sub": str(subject), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
