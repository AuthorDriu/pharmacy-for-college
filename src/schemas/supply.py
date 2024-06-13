from typing import Optional
from pydantic import BaseModel, Field


class Supplier(BaseModel):
    id: Optional[int] = None
    name: str


class Supply(BaseModel):
    id: Optional[int] = None
    supplier: int
    product: int
