from typing import Any

from src.product import Product


def test_product_init(some_product: Product) -> None:
    """Тестирование атрибутов класса Product"""
    assert some_product.name == "Пояс тк"
    assert some_product.description == "Широкий, на резинке"
    assert some_product.price == 1000.0
    assert some_product.quantity == 7


def test_product_str(some_product: Product, some_other_product: Product) -> None:
    """Тестирование на отображение класса Product в формате строки"""
    assert str(some_product) == "Пояс тк, 1000.0 руб. Остаток: 7 шт."
    assert str(some_other_product) == "Test product, 500.0 руб. Остаток: 10 шт."


def test_product_add(some_product: Product, some_other_product: Product) -> None:
    """Тестирование на сложение двух продуктов и получение их общей стоимости"""
    total_amount = some_product + some_other_product
    assert total_amount == 12000.0


def test_product_new_product(product_dict: dict[str, Any]) -> None:
    """Тестирование на добавление нового продукта"""
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Test product"
    assert new_product.description == "Test description"
    assert new_product.price == 100.0
    assert new_product.quantity == 999


def test_product_price_setter(capsys, monkeypatch) -> None:
    new_product = Product.new_product(
        {"name": "Test product", "description": "Test description", "price": 100.0, "quantity": 999}
    )
    assert new_product.price == 100.0

    new_product.price = -222.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert new_product.price == 100.0

    monkeypatch.setattr("builtins.input", lambda _: "y")
    new_product.price = 88
    assert new_product.price == 88
