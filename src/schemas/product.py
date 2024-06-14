from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=250)
    description: Optional[str] = None
    cost: float
    image: Optional[str] = None
    quantity: int = Field(ge=0, default=0)
