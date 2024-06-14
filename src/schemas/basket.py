from typing import Optional, Tuple, List
from pydantic import BaseModel, Field


class BasketRecord(BaseModel):
    """Хранит в себе информацию о конеретной записи в таблице корзины"""
    id: Optional[int] = None
    customer: int
    product: int
    quantity: int


class Basket(BaseModel):
    """Хранит все товары в корзине конкретного пользователя"""
    customer: int
    products: str


def basket_from_list(basketrecs: List[BasketRecord]) -> Basket:
    raise NotImplementedError   