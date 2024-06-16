from typing import Annotated

from src.repositories.user import CustomersRepository, EmployeesRepository
from src.services.user import UserService, get_employee_service
from src.services.login import LoginService, get_login_service
from src.schemas.token import Token
from src.schemas.user import User, Role

from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from pydantic import BaseModel, EmailStr


router = APIRouter(
    prefix="/employee",
    tags=["auth"]
)


class NewEmployee(BaseModel):
    fullname: str
    email: EmailStr
    role: Role


@router.post("/register")
def register_new_customer(
    new_user: Annotated[NewEmployee, Depends()],
    user_service: Annotated[UserService, Depends(get_employee_service)]
):
    id = user_service.register(new_user)
    return { "uid": id }


@router.post("/before-token")
def auth_first_step(
    email: EmailStr,
    login_service:  Annotated[LoginService, Depends(get_login_service)],
    user_service: Annotated[UserService, Depends(get_employee_service)]
):
    user = user_service.authenticate(email)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Пользователь не зарегистрирован")
    
    cid = login_service.send_code(user)
    return { "ok": True }


@router.get("/token")
def get_access_token_for_customer(
    email: EmailStr,
    code: str,
    login_service:  Annotated[LoginService, Depends(get_login_service)],
    user_service: Annotated[NewEmployee, Depends(get_employee_service)]
) -> Token:
    if not user_service.exitst(email):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Такого пользователя не существует")
    
    user = user_service.authenticate(email)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            "Несмотря на то, что пользователь есть в базе, его не удолось найти")

    if not login_service.check_code(user, code):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Сначала /before-token")

    token = user_service.create_access_token(user.fullname, user.email)
    return token