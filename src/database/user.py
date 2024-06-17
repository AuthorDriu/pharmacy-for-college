from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.database.db import Base


class CustomersTable(Base):
    __tablename__ = "Customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)


from src.schemas.user import Role


class EmployeesTable(Base):
    __tablename__ = "Employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    role: Mapped[Role] = mapped_column(nullable=False)


class UserLoginDataTable(Base):
    __tablename__ = "UserLoginData"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(length=6), nullable=False)
