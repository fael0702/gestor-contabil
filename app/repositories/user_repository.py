from app.entities.user import UserDb
from sqlalchemy.orm import Session


def create_user_db(new_user: UserDb, db: Session):
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
