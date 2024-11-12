import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def some_product():
    return Product("Пояс", "Широкий, на резинке", 1000.0, 7)


@pytest.fixture
def first_category():
    category_1 = Category(
        "Украшения",
        "Любовь каждой женщины",
        [
            Product("Ожерелье", "Красивое ожерелье из морского жемчуга", 10000.0, 2),
            Product("Браслет", "Изящный пластинчатый браслет из натуральных камней", 3500.0, 3),
            Product("Кольцо", "Серебряное кольцо с сияющим камнем", 2500.0, 5),
        ],
    )
    return category_1


@pytest.fixture
def second_category():
    category_2 = Category(
        "Аксессуары",
        "Подойдут для любого наряда",
        [
            Product("Сумка", "Сумка из натуральной кожи", 7000.0, 1),
            Product("Пояс", "Тканевый, с крепкой пряжкой", 1500.0, 11),
        ],
    )
    return category_2


@pytest.fixture
def product_dict():
    return {"name": "Test product", "description": "Test description", "price": 100.0,
         "quantity": 999}
