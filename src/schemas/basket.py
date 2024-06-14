from typing import Optional, Tuple, List
from pydantic import BaseModel, Field


class BasketRecord(BaseModel):
    """Хранит в себе информацию о конеретной записи в таблице корзин"""
    id: Optional[int] = None
    customer: int
    product: int
    quantity: int


class Basket(BaseModel):
    """Хранит все товары в корзине конкретного пользователя"""
    customer: int
    products: str
    cost: float