from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated
from app.entities.user import UserBase

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

load_dotenv()

KEY = os.getenv("KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: Annotated[str, Depends(oauth2_scheme)]) -> UserBase:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = jwt.decode(token, KEY, algorithms=[ALGORITHM])
    user_id = payload.get("id")
    username = payload.get("username")
    email = payload.get("email")
    exp = payload.get("exp")

    if user_id is None:
        raise credentials_exception

    if exp is not None and datetime.fromtimestamp(exp, timezone.utc) <= datetime.now(timezone.utc):
        raise credentials_exception

    return UserBase(id=user_id, username=username, email=email)
