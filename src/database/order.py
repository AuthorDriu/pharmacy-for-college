from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, BLOB, String
from src.database.db import Base


class OrdersTable(Base):
    __tablename__ = "Orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer: Mapped[int] = mapped_column(ForeignKey("Customers.id", ondelete="CASCADE"), nullable=False)
    order: Mapped[str] = mapped_column(String, nullable=False) # Формат "order_1*quantity_1;...;order_n*quantity_n"


class BasketTable(Base):
    __tablename__ = "Basket"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer: Mapped[int] = mapped_column(ForeignKey("Customers.id", ondelete="CASCADE"), nullable=False)
    product: Mapped[int] = mapped_column(ForeignKey("Products.id", ondelete="CASCADE"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)