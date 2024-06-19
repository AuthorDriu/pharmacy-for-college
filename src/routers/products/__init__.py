from typing import Annotated, List

from fastapi import APIRouter, Request, Depends, HTTPException
from starlette import status

from src.services.products import ProductsService, get_products_service
from src.services.user import UserService, get_customer_service

from src.schemas.product import Product

from .customer import router as customer_router
from .employee import router as employee_router


router = APIRouter(
    prefix="/products",
    tags=["products"]
)


router.include_router(customer.router)
router.include_router(employee.router)


@router.get("/pages")
def get_page(
    page: int,
    page_size: int,
    product_service: Annotated[ProductsService, Depends(get_products_service)],
) -> List[Product]:
    return product_service.page(page, page_size)


@router.get("/get/{id}")
def get_product(
    id: int,
    product_service: Annotated[ProductsService, Depends(get_products_service)]
) -> Product:
    product = product_service.get(id)
    if not product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Продукт не найден")
    return product

