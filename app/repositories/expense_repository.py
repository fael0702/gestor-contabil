from sqlalchemy.orm import Session
from app.entities.expense import ExpenseDb


def create_expense_db(new_expense: ExpenseDb, db: Session):
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
