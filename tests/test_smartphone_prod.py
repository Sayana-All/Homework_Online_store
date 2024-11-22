import pytest

from src.smartphone_prod import Smartphone


def test_smartphone_prod_init(some_smartphone_1: Smartphone, some_smartphone_2: Smartphone) -> None:
    """Тестирование атрибутов класса Smartphone"""
    assert some_smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert some_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert some_smartphone_1.price == 180000.0
    assert some_smartphone_1.quantity == 5
    assert some_smartphone_1.efficiency == 95.5
    assert some_smartphone_1.model == "S23 Ultra"
    assert some_smartphone_1.memory == 256
    assert some_smartphone_1.color == "Серый"

    assert some_smartphone_2.name == "Xiaomi Redmi Note 11"
    assert some_smartphone_2.description == "1024GB, Синий"
    assert some_smartphone_2.price == 31000.0
    assert some_smartphone_2.quantity == 14
    assert some_smartphone_2.efficiency == 90.3
    assert some_smartphone_2.model == "Note 11"
    assert some_smartphone_2.memory == 1024
    assert some_smartphone_2.color == "Синий"


def test_smartphone_prod_add(some_smartphone_1: Smartphone, some_smartphone_2: Smartphone) -> None:
    """Тестирование на сложение двух продуктов одного класса и получение их общей стоимости"""
    assert some_smartphone_1 + some_smartphone_2 == 1334000.0


def test_smartphone_prod_add_error(some_smartphone_2: Smartphone) -> None:
    """Тестирование на некорректное сложение двух объектов"""
    with pytest.raises(TypeError):
        some_smartphone_2 + 12
