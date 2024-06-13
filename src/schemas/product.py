from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=250)
    description: Optional[str]
    cost: float
    image: Optional[str]
    quantity: int = Field(qe=0)
