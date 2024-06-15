from abc import ABC, abstractmethod
from typing import Optional, List

from src.database.db import session_factory as _session_factory
from src.database.supply import SuppliesTable

from src.schemas.supply import Supply, Supplier


class ISuppliesRepository(ABC):
    @abstractmethod
    def add(self, supply: Supply) -> int:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def delete_all_by_supplier(self, supplier: Supplier):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[Supply]:
        pass

    @abstractmethod
    def find_all_by_supplier(self, supplier: Supplier) -> List[Supply]:
        pass


class SuppliesRepository(ISuppliesRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory

    def add(self, supply: Supply) -> int:
        with self.session_factory() as session:
            new_supply = SuppliesTable(**supply.model_dump())
            session.add(new_supply)
            session.commit()
            return new_supply.id

    def delete(self, id: int):
        with self.session_factory() as session:
            supply = session.get(SuppliesTable, id)
            if supply:
                session.delete(supply)
                session.commit()

    def delete_all_by_supplier(self, supplier: Supplier):
        with self.session_factory() as session:
            supplies = (
                session
                .query(SuppliesTable)
                .filter(SuppliesTable.supplier == supplier.id)
                .all()
            )
            if len(supplies) > 0:
                for supply in supplies:
                    session.delete(supply)
                session.commit()

    def find(self, id: int) -> Optional[Supply]:
        with self.session_factory() as session:
            supply = session.get(SuppliesTable, id)
            if not supply:
                return None
            return SuppliesRepository.to_scheme(supply)

    def find_all_by_supplier(self, supplier: Supplier) -> List[Supply]:
        with self.session_factory() as session:
            supplies = (
                session
                .query(SuppliesTable)
                .filter(SuppliesTable.supplier == supplier.id)
                .all()
            )
            return [SuppliesRepository.to_scheme(supply) for supply in supplies]

    @staticmethod
    def to_scheme(supply: SuppliesTable) -> Supply:
        return Supply(
            id=supply.id,
            supplier=supply.supplier,
            product=supply.product
        )