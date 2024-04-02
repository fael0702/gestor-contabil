from typing import Optional

from app.entities.user import UserDb, UserLogin
from sqlalchemy.orm import Session


def create_user_db(new_user: UserDb, db: Session):
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_name(username: str, db: Session) -> Optional[UserLogin]:
    user = (
        db.query(UserDb)
        .filter(UserDb.username == username)
        .first()
    )

    if user is None:
        return None

    return UserLogin(id=user.id, username=user.username, email=user.email, rule=user.rule.value, password=user.password)
