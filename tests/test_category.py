def test_category(first_category, second_category):
    """Тестирование атрибутов класса Category"""
    assert first_category.name == "Украшения"
    assert first_category.description == "Любовь каждой женщины"

    assert second_category.name == "Аксессуары"
    assert second_category.description == "Подойдут для любого наряда"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_products_property(first_category, second_category):
    """Тестирование геттера на выведение строки списка продуктов класса Категорий"""
    assert first_category.products == (
        "Ожерелье, 10000.0 руб. Остаток: 2 шт.\n"
        "Браслет, 3500.0 руб. Остаток: 3 шт.\n"
        "Кольцо, 2500.0 руб. Остаток: 5 шт.\n"
    )
    assert second_category.products == ("Сумка, 7000.0 руб. Остаток: 1 шт.\nПояс кож, 1500.0 руб. Остаток: 11 шт.\n")


def test_product_list_property(first_category, second_category):
    """Тестирование геттера на получение списка продуктов и взаимодействия с ним"""
    assert len(first_category.product_list) == 3
    assert len(second_category.product_list) == 2


def test_add_product(second_category, some_product):
    """Тест на добавление нового продукта в список через категорию"""
    assert second_category.products == ("Сумка, 7000.0 руб. Остаток: 1 шт.\nПояс кож, 1500.0 руб. Остаток: 11 шт.\n")
    second_category.add_product(some_product)
    assert second_category.products == (
        "Сумка, 7000.0 руб. Остаток: 1 шт.\n"
        "Пояс кож, 1500.0 руб. Остаток: 11 шт.\n"
        "Пояс тк, 1000.0 руб. Остаток: 7 шт.\n"
    )
