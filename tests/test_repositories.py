import prepare
from src.database.db import create_database, drop_database

from src.repositories.user import CustomersRepository, EmployeesRepository
from src.repositories.product import ProductsRepository
from src.repositories.order import OrderRepository
from src.repositories.basket import BasketRepository
from src.repositories.supplier import SuppliersRepository
from src.repositories.supply import SuppliesRepository

from src.schemas.user import Customer, Employee, Role
from src.schemas.product import Product
from src.schemas.order import Order
from src.schemas.basket import BasketRecord, Basket
from src.schemas.supply import Supplier, Supply


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


#=========================================================================
#                         BasketRepository
#=========================================================================


def test_add_basketrec():
    assert BasketRepository().add(
        BasketRecord(
            customer=1,
            product=10,
            quantity=1
        )
    ) == 1
    assert BasketRepository().add(
        BasketRecord(
            customer=1,
            product=9,
            quantity=2
        )
    ) == 2
    assert BasketRepository().add(
        BasketRecord(
            customer=1,
            product=8,
            quantity=3
        )
    ) == 3

def test_find_basketrec():
    assert BasketRepository().find(1).id == 1


def test_find_all_basket_by_user():
    assert BasketRepository().find_all_by_user(
        Customer(
            id=1,
            fullname="Ладно, это уже я",
            email="authordriu@yandex.ru"
        )
    ).products == "10*1;9*2;8*3"


def test_delete_basketrec():
    BasketRepository().delete(3)
    assert BasketRepository().find(3) is None


def test_delete_all_basketrecs_by_user():
    user = Customer(
        id=1,
        fullname="ЭЭЭЭЭЭЭ ВСМЫСЛЕ",
        email="authordriu@yandex.ru"
    )
    BasketRepository().delete_all_by_user(user)
    assert BasketRepository().find_all_by_user(user) is None


#=========================================================================
#                         BasketRepository
#=========================================================================


def test_add_supplier():
    assert SuppliersRepository().add(
        Supplier(
            name="ООО \"Cactus Infrastructure\""
        )
    ) == 1


def test_find_supplier():
    assert SuppliersRepository().find(1).id == 1


def test_find_by_name():
    assert SuppliersRepository().find_by_name(
        "ООО \"Cactus Infrastructure\""
    ).id == 1


def test_delete_supplier():
    SuppliersRepository().delete(1)
    assert SuppliersRepository().find(1) is None


#=========================================================================
#                         BasketRepository
#=========================================================================


def test_add_supply():
    assert SuppliesRepository().add(
        Supply(
            supplier=1,
            product=1
        )
    ) == 1
    assert SuppliesRepository().add(
        Supply(
            supplier=1,
            product=2
        )
    ) == 2
    assert SuppliesRepository().add(
        Supply(
            supplier=1,
            product=3
        )
    ) == 3


def test_find_supply():
    assert SuppliesRepository().find(1).supplier == 1


def test_find_all_by_supplier():
    assert len(
        SuppliesRepository()
        .find_all_by_supplier(
            Supplier(
                id=1,
                name="ООО \"Cactus Infrastructure\""
            )
        )
    ) == 3


def test_delete_supply():
    SuppliesRepository().delete(1)
    assert SuppliesRepository().find(1) is None


def test_delete_all_supplies_by_supplier():
    SuppliesRepository().delete_all_by_supplier(
        Supplier(
            id=1,
            name="ООО \"Cactus Infrastructure\""
        )
    )
    assert len(
        SuppliesRepository()
        .find_all_by_supplier(
            Supplier(
                id=1,
                name="ООО \"Cactus Infrastructure\""
            )
        )
    ) == 0


def test_dropping_database():
    drop_database()