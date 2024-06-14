from typing import Optional, Tuple
from pydantic import BaseModel, Field


class Order(BaseModel):
    id: Optional[int] = None
    customer: int
    order: Tuple[str, ...]
    cost: float