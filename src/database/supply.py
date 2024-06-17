from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.database.db import Base


class SuppliersTable(Base):
    __tablename__ = "Suppliers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)


class SuppliesTable(Base):
    __tablename__ = "Supplies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    supplier: Mapped[int] = mapped_column(ForeignKey("Suppliers.id", ondelete="CASCADE"), nullable=False)
    product: Mapped[int] = mapped_column(ForeignKey("Products.id", ondelete="CASCADE"), nullable=False)
