from typing import List
from src.repositories.product import IProductsRepository, ProductsRepository
from src.schemas.product import Product


class ProductsService:
    def __init__(self, products_repository: IProductsRepository):
        self.repo = products_repository
    
    def add_new_product(self, product: Product) -> int:
        return self.repo.add(product)
    
    def get(self, id) -> Product:
        return self.repo.find(id)

    def page(self, page: int, page_size: int) -> List[Product]:
        return self.repo.find_page_of_present(page, page_size)
    
    def delete(self, id: int):
        self.repo.delete(id)


def get_products_service():
    yield ProductsService(ProductsRepository())