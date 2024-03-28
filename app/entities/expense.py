from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func

from .base import Base


class ExpenseDb(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )
    categoria: Mapped[str] = mapped_column(nullable=False)
    valor: Mapped[int] = mapped_column(nullable=False)
    metodo: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=True)
    mes: Mapped[int] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("UserDb", back_populates="expenses")


class ExpenseBase(BaseModel):
    id: int
    cartegoria: str
    valor: int
    metodo: str
    descricao: str
    mes: int
    ano: int


class ExpenseCreate(BaseModel):
    cartegoria: str
    valor: int
    metodo: str
    descricao: str
    mes: int
    ano: int
