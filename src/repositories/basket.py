from abc import ABC, abstractmethod
from typing import Optional


from src.database.db import session_factory as _session_factory
from src.database.order import BasketTable
from src.schemas.basket import BasketRecord, Basket


class IBasketRepository(ABC):
    pass