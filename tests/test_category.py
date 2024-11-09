def test_category(first_category, second_category):
    """Тестирование класса Category"""
    assert first_category.name == "Украшения"
    assert first_category.description == "Любовь каждой женщины"
    assert len(first_category.products) == 3

    assert second_category.name == "Аксессуары"
    assert second_category.description == "Подойдут для любого наряда"
    assert len(second_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5

