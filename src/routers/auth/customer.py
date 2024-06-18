from typing import Annotated

from src.repositories.user import CustomersRepository, EmployeesRepository
from src.services.user import UserService, get_customer_service
from src.services.login import LoginService, get_login_service
from src.schemas.user import User
from src.schemas.token import Token

from fastapi import APIRouter, Response, HTTPException, Depends
from starlette import status

from pydantic import BaseModel, EmailStr


router = APIRouter(
    prefix="/customer",
    tags=["auth"]
)


class NewUser(BaseModel):
    fullname: str
    email: EmailStr


@router.post("/register")
def register_new_customer(
    new_user: Annotated[NewUser, Depends()],
    user_service: Annotated[UserService, Depends(get_customer_service)]
):
    id = user_service.register(new_user)
    return { "uid": id }


@router.post("/before_token")
def auth_first_step(
    email: EmailStr,
    login_service:  Annotated[LoginService, Depends(get_login_service)],
    user_service: Annotated[UserService, Depends(get_customer_service)]
):
    user = user_service.authenticate(email)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Пользователь не зарегистрирован")
    
    cid = login_service.send_code(user)
    return { "ok": True }


@router.get("/token")
def get_access_token_for_customer(
    response: Response,
    email: EmailStr,
    code: str,
    login_service:  Annotated[LoginService, Depends(get_login_service)],
    user_service: Annotated[UserService, Depends(get_customer_service)]
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
    response.set_cookie(key="Token", value=token.model_dump_json())
    
    return token