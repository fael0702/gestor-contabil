from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime
from typing import List

from .base import Base
from .expense import ExpenseDb
from .revenue import RevenueDb


class UserDb(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)

    expenses: Mapped[List["ExpenseDb"]] = relationship(back_populates="user")
    revenues: Mapped[List["RevenueDb"]] = relationship(back_populates="user")


class UserBase(BaseModel):
    id: int
    username: str
    email: str
    rule: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    rule: str


class UserLogin(BaseModel):
    id: int
    username: str
    email: str
    rule: str
    password: str
