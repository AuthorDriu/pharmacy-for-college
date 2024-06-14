from abc import ABC, abstractmethod
from typing import Optional

from src.database.db import session_factory as _session_factory
from src.database.user import CustomersTable, EmployeesTable
from src.schemas.user import User, Customer, Employee 


class IUsersRepository(ABC):
    @abstractmethod
    def add(self, new_user: User) -> int:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def find(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass


class CustomersRepository(IUsersRepository):
    def __init__(self, session_factory = _session_factory):
        self.session_factory = session_factory
    
    def add(self, new_user: Customer) -> int:
        with self.session_factory() as session:
            new_customer = CustomersTable(**new_user.model_dump())
            session.add(new_customer)
            session.commit()
            return new_customer.id
    
    def delete(self, id: int):
        with self.session_factory() as session:
            customer = session.get(CustomersTable, id)
            if customer:
                session.delete(customer)
                session.commit()
    
    def find(self, id: int) -> Optional[Customer]:
        with self.session_factory() as session:
            customer = session.get(CustomersTable, id)
            if not customer:
                return None
            return CustomersRepository.to_scheme(customer)
    
    def find_by_email(self, email: str) -> Optional[Customer]:
        with self.session_factory() as session:
            customer = (
                session
                .query(CustomersTable)
                .filter(CustomersTable.email == email)
                .one_or_none()
            )
            if not customer:
                return None
            return CustomersRepository.to_scheme(customer)
    
    @staticmethod
    def to_scheme(customer: CustomersTable) -> Customer:
        return Customer(
            id=customer.id,
            fullname=customer.fullname,
            email=customer.email
        )


class EmployeesRepository(IUsersRepository):
    def __init__(self, session_factory = _session_factory):
        self.session_factory = session_factory

    def add(self, new_user: Employee) -> int:
        with self.session_factory() as session:
            employee = EmployeesTable(**new_user.model_dump())
            session.add(employee)
            session.commit()
            return employee.id
    
    def delete(self, id: int):
        with self.session_factory() as session:
            employee = session.get(EmployeesTable, id)
            if employee:
                session.delete(employee)
                session.commit()
    
    def find(self, id: int) -> Optional[Employee]:
        with self.session_factory() as session:
            employee = session.get(EmployeesTable, id)
            if not employee:
                return None
            return EmployeesRepository.to_scheme(employee)
    
    def find_by_email(self, email: str) -> Optional[Employee]:
        with self.session_factory() as session:
            employee = (
                session
                .query(EmployeesTable)
                .filter(EmployeesTable.email == email)
                .one_or_none()
            )
            if not employee:
                return None
            return EmployeesRepository.to_scheme(employee)
    
    @staticmethod
    def to_scheme(employee: EmployeesTable) -> Employee:
        return Employee(
            id=employee.id,
            fullname=employee.fullname,
            email=employee.email,
            role=employee.role
        )