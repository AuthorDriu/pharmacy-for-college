from typing import Annotated, List

from fastapi import APIRouter, Request, Depends, HTTPException
from starlette import status

from src.services.products import ProductsService, get_products_service
from src.services.user import UserService, get_customer_service

from src.schemas.product import Product


router = APIRouter(
    prefix="/customer"
)