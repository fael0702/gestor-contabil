from typing import Annotated

import bcrypt
from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import create_jwt_token

from app.database import get_db
from app.repositories.user_repository import create_user_db, get_user_by_name
from app.entities.user import UserDb
from app.services.user_service import create_password_hash
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post("")
def create_user(username: str, email: str, password: str,
                db: Session = Depends(get_db)):
    password = create_password_hash(password)
    new_user = UserDb(username=username, email=email, password=password)
    created_user = create_user_db(new_user, db)
    return created_user


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = get_user_by_name(form_data.username, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if bcrypt.checkpw(form_data.password.encode('utf-8'), user.password.encode('utf-8')):
        token_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "rule": user.rule
        }

        access_token = create_jwt_token(data=token_data)
        return access_token
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
