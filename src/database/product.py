from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.database.db import Base


class ProductsTable(Base):
    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    description: Mapped[Optional[str]]
    cost: Mapped[float] = mapped_column(nullable=False)
    image: Mapped[Optional[str]]
    quantity: Mapped[int] = mapped_column(nullable=False)
