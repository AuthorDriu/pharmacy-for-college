from typing import Union, Annotated, Optional

from fastapi import APIRouter, Depends

from .customer import router as customer_router
from .employee import router as employee_router

from src.services.user import UserService, get_customer_service, get_employee_service

from src.schemas.token import Token
from src.schemas.user import User, Customer, Employee


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


router.include_router(customer_router)
router.include_router(employee_router)



@router.post("/checkme")
def check_jwt_access(
    token: Token,
    customer_service: Annotated[UserService, Depends(get_customer_service)],
    employee_service: Annotated[UserService, Depends(get_employee_service)]
) -> Optional[Union[Customer, Employee]]:
    c = customer_service.current_user(token.access_token)
    if c:
        return c

    e = employee_service.current_user(token.access_token)
    if e:
        return e
    
    return None
