from app.database import get_db
from app.repositories.user_repository import create_user_db
from app.entities.user import UserDb
from app.services.user_service import create_password_hash
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

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
