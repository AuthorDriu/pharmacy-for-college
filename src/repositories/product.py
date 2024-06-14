from abc import ABC, abstractmethod
from typing import Optional

from src.database.db import session_factory as _session_factory
from src.database.product import ProductsTable
from src.schemas.product import Product

# Я не думаю, что оно пригодится, но вдруг?
class IProductsRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> int:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[Product]:
        pass


class ProductsRepository(IProductsRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory

    def add(self, product: Product) -> int:
        with self.session_factory() as session:
            new_product = ProductsTable(**product.model_dump())
            session.add(new_product)
            session.commit()
            return new_product.id
    
    def delete(self, id: int):
        with self.session_factory() as session:
            product = session.get(ProductsTable, id)
            if product:
                session.delete(product)
                session.commit()
    
    def find(self, id: int) -> Optional[Product]:
        with self.session_factory() as session:
            product = session.get(ProductsTable, id)
            if not product:
                return None
            return ProductsRepository.to_scheme(product)
    
    @staticmethod
    def to_scheme(product: ProductsTable) -> Product:
        return Product(
            id=product.id,
            title=product.title,
            description=product.description,
            cost=product.cost,
            image=product.image,
            quantity=product.quantity
        )