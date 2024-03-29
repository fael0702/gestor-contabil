from datetime import datetime
from typing import Annotated
from app.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.entities.expense import ExpenseDb
from app.entities.user import UserDb
from app.repositories.revenue_repository import create_revenue_db
from app.services.auth_service import verify_token

router = APIRouter(
    prefix='/expense',
    tags=['Expense']
)


@router.post("")
def create_expense(categoria: str, valor: float, metodo: str,
                   current_user: Annotated[UserDb, Depends(verify_token)],
                   db: Session = Depends(get_db),
                   mes: int = datetime.now().month,
                   ano: int = datetime.now().year,
                   descricao: str = None):
    new_expense = ExpenseDb(categoria=categoria, valor=valor, metodo=metodo, mes=mes, ano=ano, descricao=descricao,
                            user_id=current_user.id)
    created_user = create_revenue_db(new_expense, db)
    return created_user
