from src.repositories.user import CustomersRepository, EmployeesRepository
from src.services.user import UserService
from src.schemas.token import Token

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter(
    prefix="employee/",
    tags=["auth"]
)