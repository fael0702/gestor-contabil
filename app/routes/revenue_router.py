from datetime import datetime
from typing import Annotated
from app.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.entities.revenue import RevenueDb
from app.entities.user import UserDb
from app.repositories.revenue_repository import create_revenue_db
from app.services.auth_service import verify_token

router = APIRouter(
    prefix='/revenue',
    tags=['revenue']
)


@router.post("")
def create_revenue(categoria: str, valor: float, origem: str,
                   current_user: Annotated[UserDb, Depends(verify_token)],
                   db: Session = Depends(get_db),
                   mes: int = datetime.now().month,
                   ano: int = datetime.now().year,
                   descricao: str = None):
    new_revenue = RevenueDb(categoria=categoria, valor=valor, origem=origem, mes=mes, ano=ano, descricao=descricao)
    created_user = create_revenue_db(new_revenue, db)
    return created_user
