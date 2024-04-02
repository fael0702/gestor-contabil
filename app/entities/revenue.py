from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func

from .base import Base


class RevenueDb(Base):
    __tablename__ = "revenues"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )
    categoria: Mapped[str] = mapped_column(nullable=False)
    valor: Mapped[float] = mapped_column(nullable=False)
    origem: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=True)
    mes: Mapped[int] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("UserDb", back_populates="revenues")


class RevenueBase(BaseModel):
    id: int
    cartegoria: str
    valor: int
    origem: str
    descricao: str
    mes: int
    ano: int


class RevenueCreate(BaseModel):
    cartegoria: str
    valor: int
    origem: str
    descricao: str
    mes: int
    ano: int
