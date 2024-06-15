from fastapi import APIRouter

from .customer import router as customer_router
from .employee import router as employee_router


router = APIRouter(
    prefix="auth/",
    tags=["auth"]
)


router.include_router(customer_router)
router.include_router(employee_router)