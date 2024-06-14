from abc import ABC, abstractmethod
from typing import Optional, List

from src.database.db import session_factory as _session_factory
from src.database.order import OrdersTable
from src.schemas.basket import Basket
from src.schemas.order import Order
from src.schemas.user import User


class IOrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> int:
        pass

    @abstractmethod
    def add_from_basket(self, basket: Basket) -> int:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[Order]:
        pass

    @abstractmethod
    def find_all_by_user(self, user: User) -> List[Order]:
        pass


class OrderRepository(IOrderRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory
    
    def add(self, order: Order) -> int:
        with self.session_factory() as session:
            new_order = OrdersTable(
                customer=order.customer,
                order=";".join(order.order),
            )
            session.add(new_order)
            session.commit()
            return new_order.id
    
    def add_from_basket(self, basket: Basket) -> int:
        with self.session_factory() as session:
            new_order = OrdersTable(
                customer=basket.customer,
                order=basket.products,
            )
            session.add(new_order)
            session.commit()
            return new_order.id
    
    def delete(self, id: int):
        with self.session_factory() as session:
            order = session.get(OrdersTable, id)
            if order:
                session.delete(order)
                session.commit()

    def find(self, id: int) -> Optional[Order]:
        with self.session_factory() as session:
            order = session.get(OrdersTable, id)
            if not order:
                return None
            return OrderRepository.to_scheme(order)

    def find_all_by_user(self, user: User) -> List[Order]:
        with self.session_factory() as session:
            orders = (
                session
                .query(OrdersTable)
                .filter(OrdersTable.customer == user.id)
                .all()
            )
            if not orders:
                return None
            return [OrderRepository.to_scheme(order) for order in orders]
    
    @staticmethod
    def to_scheme(order: OrdersTable) -> Order:
        return Order(
            id=order.id,
            customer=order.customer,
            order=tuple(order.order.split(';')),
        )
