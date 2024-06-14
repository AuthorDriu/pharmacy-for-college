import prepare
from src.database.db import create_database, drop_database

from src.repositories.user import CustomersRepository, EmployeesRepository
from src.repositories.product import ProductsRepository
from src.repositories.order import OrderRepository

from src.schemas.user import Customer, Employee, Role
from src.schemas.product import Product
from src.schemas.order import Order
from src.schemas.basket import BasketRecord, Basket


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


#=========================================================================
#                         ProductsRepository
#=========================================================================


def test_add_product():
    assert ProductsRepository().add(
        Product(
            title="Some product",
            description="The description of some product",
            cost=150.99,
            quantity=1
        )
    ) == 1


def test_get_product():
    assert ProductsRepository().find(1).id == 1


def test_delete_product():
    ProductsRepository().delete(1)
    assert ProductsRepository().find(1) is None


#=========================================================================
#                         OrdersRepository
#=========================================================================


def test_add_order():
    assert OrderRepository().add(
        Order(
            customer=1,
            order=("1*2","2*1"),
            cost=2004
        )
    ) == 1


def test_add_order_from_basket():
    assert OrderRepository().add_from_basket(
        Basket(
            customer=1,
            products="1*2;6*3",
            cost=5344
        )
    ) == 2


def test_find_all_orders_by_user():
    assert len(
        OrderRepository().find_all_by_user(
            Customer(
                id=1,
                fullname="Это точно не я",
                email="authordriu@yandex.ru"
            )
        )
    ) == 2


def test_delete_order():
    OrderRepository().delete(1)
    OrderRepository().delete(2)
    assert OrderRepository().find(1) is None
    assert OrderRepository().find(2) is None


def test_dropping_database():
    drop_database()