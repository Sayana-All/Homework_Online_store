from typing import Any

import pytest

from src.category import Category
from src.lawngrass_prod import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone_prod import Smartphone


@pytest.fixture
def some_product() -> Any:
    return Product("Пояс тк", "Широкий, на резинке", 1000.0, 7)


@pytest.fixture
def some_other_product() -> Any:
    return Product("Test product", "Test description", 500.0, 10)


@pytest.fixture
def first_category() -> Any:
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
def second_category() -> Any:
    category_2 = Category(
        "Аксессуары",
        "Подойдут для любого наряда",
        [
            Product("Сумка", "Сумка из натуральной кожи", 7000.0, 1),
            Product("Пояс кож", "Кожаный, с крепкой пряжкой", 1500.0, 11),
        ],
    )
    return category_2


@pytest.fixture
def product_dict() -> dict[str, Any]:
    return {"name": "Test product", "description": "Test description", "price": 100.0, "quantity": 999}


@pytest.fixture
def prod_iterator(second_category: Any) -> Any:
    return ProductIterator(second_category)


@pytest.fixture
def some_smartphone_1() -> Any:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    return smartphone1


@pytest.fixture
def some_smartphone_2() -> Any:
    smartphone2 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    return smartphone2


@pytest.fixture
def some_grass_1() -> Any:
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return grass1


@pytest.fixture
def some_grass_2() -> Any:
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return grass2


@pytest.fixture
def category_empty() -> Any:
    return Category("Пустая категория", "Категория без продуктов", [])
