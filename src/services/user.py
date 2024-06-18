from typing import Optional

from src.repositories.user import IUsersRepository, CustomersRepository, EmployeesRepository
from src.schemas.user import User
from src.schemas.token import Token

from src.config import auth_settings

from jose import jwt, JWTError

from fastapi import HTTPException
from starlette import status


class UserService:
    def __init__(self, user_repository: IUsersRepository):
        self.repo = user_repository
        self.secret_key = auth_settings.SECRET_KEY
        self.algorithm = auth_settings.ALGORITHM
    
    def register(self, user: User) -> int:
        uid = self.repo.add(user)
        return uid
    

    def user_from_token(self, request) -> Optional[User]:
        token = Token.model_validate_json(request.cookies["Token"])
        user = self.current_user(token.access_token)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        return user


    def authenticate(self, email: str) -> Optional[User]:
        # Проверяю есть ли данный пользователь в базе данных
        user = self.repo.find_by_email(email)
        return user
    
    def exitst(self, email: str) -> bool:
        """Проверяет существует ли пользователь в базе данных"""
        return self.repo.find_by_email(email) is not None

    def create_access_token(self, fullname: str, email: str) -> Token:
        encode = { "fullname": fullname, "email": email }
        return Token(
            access_token=jwt.encode(encode, self.secret_key, algorithm=self.algorithm),
            token_type="bearer"
        )
    
    def current_user(self, token: str) -> Optional[User]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=self.algorithm)
            return self.authenticate(payload["email"])
        except JWTError:
            return None


def get_employee_service():
    yield UserService(EmployeesRepository())


def get_customer_service():
    yield UserService(CustomersRepository())
