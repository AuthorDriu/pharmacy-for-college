from abc import ABC, abstractmethod
from typing import Optional

from src.database.db import session_factory as _session_factory
from src.database.supply import SuppliersTable

from src.schemas.supply import Supplier


class ISuppliersRepository(ABC):
    @abstractmethod
    def add(self, supplier: Supplier) -> id:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[Supplier]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[Supplier]:
        pass


class SuppliersRepository(ISuppliersRepository):
    def __init__(self, session_factory=_session_factory):
        self.session_factory = session_factory

    def add(self, supplier: Supplier) -> id:
        with self.session_factory() as session:
            new_supplier = SuppliersTable(**supplier.model_dump())
            session.add(new_supplier)
            session.commit()
            return new_supplier.id

    def delete(self, id: int):
        with self.session_factory() as session:
            supplier = session.get(SuppliersTable, id)
            if supplier:
                session.delete(supplier)
                session.commit()

    def find(self, id: int) -> Optional[Supplier]:
        with self.session_factory() as session:
            supplier = session.get(SuppliersTable, id)
            if not supplier:
                return None
            return SuppliersRepository.to_scheme(supplier)

    def find_by_name(self, name: str) -> Optional[Supplier]:
        with self.session_factory() as session:
            supplier = (
                session
                .query(SuppliersTable)
                .filter(SuppliersTable.name == name)
                .one_or_none()
            )
            if not supplier:
                return None
            return SuppliersRepository.to_scheme(supplier)

    @staticmethod
    def to_scheme(supplier: SuppliersTable) -> Supplier:
        return Supplier(
            id=supplier.id,
            name=supplier.name
        )