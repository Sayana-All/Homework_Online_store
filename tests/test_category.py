from typing import Any

import pytest


def test_category(first_category: Any, second_category: Any) -> None:
    """Тестирование атрибутов класса Category"""
    assert first_category.name == "Украшения"
    assert first_category.description == "Любовь каждой женщины"

    assert second_category.name == "Аксессуары"
    assert second_category.description == "Подойдут для любого наряда"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_product_str(first_category: Any, second_category: Any) -> None:
    """Тестирование на отображение класса Category в формате строки"""
    assert str(first_category) == "Украшения, количество продуктов: 3 шт."
    assert str(second_category) == "Аксессуары, количество продуктов: 2 шт."


def test_products_property(first_category: Any, second_category: Any) -> None:
    """Тестирование геттера на выведение строки списка продуктов класса Категорий"""
    assert first_category.products == (
        "Ожерелье, 10000.0 руб. Остаток: 2 шт.\n"
        "Браслет, 3500.0 руб. Остаток: 3 шт.\n"
        "Кольцо, 2500.0 руб. Остаток: 5 шт.\n"
    )
    assert second_category.products == ("Сумка, 7000.0 руб. Остаток: 1 шт.\nПояс кож, 1500.0 руб. Остаток: 11 шт.\n")


def test_product_list_property(first_category: Any, second_category: Any) -> None:
    """Тестирование геттера на получение списка продуктов и взаимодействия с ним"""
    assert len(first_category.product_list) == 3
    assert len(second_category.product_list) == 2


def test_add_product(second_category: Any, some_product: Any) -> None:
    """Тест на добавление нового продукта в список через категорию"""
    assert second_category.products == ("Сумка, 7000.0 руб. Остаток: 1 шт.\nПояс кож, 1500.0 руб. Остаток: 11 шт.\n")
    second_category.add_product(some_product)
    assert second_category.products == (
        "Сумка, 7000.0 руб. Остаток: 1 шт.\n"
        "Пояс кож, 1500.0 руб. Остаток: 11 шт.\n"
        "Пояс тк, 1000.0 руб. Остаток: 7 шт.\n"
    )


def test_product_iterator(prod_iterator: Any) -> None:
    """Тестирование класса ProductIterator"""
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Сумка"
    assert next(prod_iterator).name == "Пояс кож"

    with pytest.raises(StopIteration):
        next(prod_iterator)
