from src.product import Product


def test_product_init(some_product):
    """Тестирование атрибутов класса Product"""
    assert some_product.name == "Пояс"
    assert some_product.description == "Широкий, на резинке"
    assert some_product.price == 1000.0
    assert some_product.quantity == 7


def test_product_new_product(product_dict) -> None:
    """Тестирование на добавление нового продукта"""
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Test product"
    assert new_product.description == "Test description"
    assert new_product.price == 100.0
    assert new_product.quantity == 999


def test_product_price_setter(capsys, monkeypatch):
    """Проверка на изменение цены"""
    new_product = Product.new_product({"name": "Test product", "description": "Test description", "price": 100.0,
         "quantity": 999})
    assert new_product.price == 100.0

    new_product.price = -222.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert new_product.price == 100.0

    monkeypatch.setattr("builtins.input", lambda _: "y")
    new_product.price = 88
    assert new_product.price == 88
