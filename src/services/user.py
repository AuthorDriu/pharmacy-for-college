from typing import Optional

from src.repositories.user import IUsersRepository, CustomersRepository, EmployeesRepository
from src.schemas.user import User
from src.schemas.token import Token

from src.config import auth_settings

from jose import jwt, JWTError


class UserService:
    def __init__(self, user_repository: IUsersRepository):
        self.repo = user_repository
        self.secret_key = auth_settings.SECRET_KEY
        self.algorithm = auth_settings.ALGORITHM
    
    def register(self, user: User) -> int:
        uid = self.repo.add(user)
        return uid
    
    def authenticate(self, email: str) -> Optional[User]:
        # Проверяю есть ли данный пользователь в базе данных
        user = self.repo.find_by_email(email)
        if not user:
            return None
        
        # Пока что здесь сразу возвращается пользователь без какой либо проверки
        # является ли пользователь собой или нет. Потом доделаю.
        return user
    
    def __create_access_token(self, fullname: str, email: str) -> Token:
        encode = { "fullname": fullname, "email": email }
        return jwt.encode(encode, self.secret_key, algorithm=self.algorithm)
    

def get_employee_service():
    yield UserService(EmployeesRepository())


def get_customer_service():
    yield UserService(CustomersRepository())
