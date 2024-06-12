from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=250)
    description: str
    cost: float
    image: str = Field(max_length=250)
    quantity: int = Field(ge=0)