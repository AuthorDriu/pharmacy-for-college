from abc import ABC, abstractmethod
from typing import Optional, List, Union


from src.database.db import session_factory as _session_factory
from src.database.order import BasketTable
from src.schemas.basket import BasketRecord, Basket
from src.schemas.user import User


class IBasketRepository(ABC):
    @abstractmethod
    def add(self, basketrec: BasketRecord) -> int:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def delete_all_by_user(self, user: User):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[BasketRecord]:
        pass

    @abstractmethod
    def find_all_by_user(self, user: User) -> Basket:
        pass


class BasketRepository(IBasketRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory
    
    def add(self, basketrec: BasketRecord) -> int:
        with self.session_factory() as session:
            new_basketrec = BasketTable(**basketrec.model_dump())
            session.add(new_basketrec)
            session.commit()
            return new_basketrec.id

    def delete(self, id: int):
        with self.session_factory() as session:
            basketrec = session.get(BasketTable, id)
            if basketrec:
                session.delete(basketrec)
                session.commit()

    def delete_all_by_user(self, user: User):
        with self.session_factory() as session:
            basketrecs = (
                session
                .query(BasketTable)
                .filter(BasketTable.customer == user.id)
                .all()
            )
            if len(basketrecs) > 0:
                for basketrec in basketrecs:
                    session.delete(basketrec)
                session.commit()

    def find(self, id: int) -> Optional[BasketRecord]:
        with self.session_factory() as session:
            basketrec = session.get(BasketTable, id)
            if not basketrec:
                return None
            return BasketRepository.to_schema(basketrec)

    def find_all_by_user(self, user: User) -> Optional[Basket]:
        with self.session_factory() as session:
            basketrecs = (
                session
                .query(BasketTable)
                .filter(BasketTable.customer == user.id)
                .all()
            )
            return BasketRepository.to_schema(basketrecs)

    @staticmethod
    def to_schema(
        basket: Union[BasketTable, List[BasketTable]]
    ) -> Union[BasketRecord, Optional[Basket]]:
        
        if isinstance(basket, BasketTable):
            return BasketRecord(
                id=basket.id,
                customer=basket.customer,
                product=basket.product,
                quantity=basket.quantity
            )

        elif isinstance(basket, list):
            if len(basket) == 0: return None
            return Basket(
                customer=basket[0].customer,
                products=";".join(list(map("*".join, [(str(basket[i].product), str(basket[i].quantity)) for i in range(len(basket))])))
            )

        else:
            raise ValueError(f"Неверно передан тип: {type(basket)}")