import prepare
from src.database.db import create_database, drop_database
from src.repositories.user import CustomersRepository, EmployeesRepository
from src.schemas.user import Customer, Employee, Role


def test_creating_database():
    create_database()


#=========================================================================
#                         CustomersRepository
#=========================================================================


def test_add_customer():
    assert CustomersRepository().add(
        Customer(
            fullname="Малышев Андрей Вячеславович",
            email="authordriu@yandex.ru"
        )
    ) == 1


def test_get_customer():
    assert CustomersRepository().find(1).email == "authordriu@yandex.ru"


def test_get_customer_by_email():
    assert CustomersRepository().find_by_email("authordriu@yandex.ru").id == 1


def test_delete_customer():
    CustomersRepository().delete(1)
    assert CustomersRepository().find(1) is None


#=========================================================================
#                         EmployeesRepository
#=========================================================================


def test_add_employee():
    assert EmployeesRepository().add(
        Employee(
            fullname="Сметанин Владимир Владимирович",
            email="grandspase@gmail.com",
            role=Role.Cleaner
        )
    ) == 1


def test_get_employee():
    assert EmployeesRepository().find(1).email == "grandspase@gmail.com"


def test_get_employee_by_email():
    assert EmployeesRepository().find_by_email("grandspase@gmail.com").id == 1


def test_delete_employee():
    EmployeesRepository().delete(1)
    assert EmployeesRepository().find(1) is None


def test_dropping_database():
    drop_database()