from typing import Annotated, List, Optional

from fastapi import APIRouter, Request, Depends, HTTPException
from starlette import status
from pydantic import BaseModel, Field

from src.services.products import ProductsService, get_products_service
from src.services.user import UserService, get_employee_service

from src.schemas.product import Product
from src.schemas.user import Employee, Role


router = APIRouter(
    prefix="/customer"
)


class NewProduct(BaseModel):
    title: str = Field(max_length=250)
    description: Optional[str] = None
    cost: float
    image: Optional[str] = None
    quantity: int = Field(ge=0, default=0)


@router.post("/add")
def add_product(
    request: Request,
    product: Annotated[NewProduct, Depends()],
    product_service: Annotated[ProductsService, Depends(get_products_service)],
    employee_service: Annotated[UserService, Depends(get_employee_service)]
):
    user: Employee = employee_service.user_from_token(request)
    if user.role != Role.Administrator:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Роль сотрудника не подходит")
    
    product_service.add_new_product(product)
    return { "ok": True }


@router.post("/delete")
def delete_product(
    request: Request,
    id: int,
    product_service: Annotated[ProductsService, Depends(get_products_service)],
    employee_service: Annotated[UserService, Depends(get_employee_service)]
):
    user: Employee = employee_service.user_from_token(request)
    if user.role != Role.Administrator:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Роль сотрудника не подходит")
    
    product_service.delete(id)
    return { "ok": True }