from typing import Annotated, List

from fastapi import APIRouter, Request, Depends

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
    request: Request,
    page: int,
    page_size: int,
    product_service: Annotated[ProductsService, Depends(get_products_service)],
) -> List[Product]:
    return product_service.page(page, page_size)