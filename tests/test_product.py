def test_product_init(some_product):
    """Тестирование класса Product"""
    assert some_product.name == "Пояс"
    assert some_product.description == "Тканевый, с крепкой пряжкой"
    assert some_product.price == 1500.0
    assert some_product.quantity == 11
