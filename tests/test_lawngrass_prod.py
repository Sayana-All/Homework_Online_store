import pytest

from src.lawngrass_prod import LawnGrass


def test_lawngrass_prod_init(some_grass_1: LawnGrass, some_grass_2: LawnGrass) -> None:
    """Тестирование атрибутов класса LawnGrass"""
    assert some_grass_1.name == "Газонная трава"
    assert some_grass_1.description == "Элитная трава для газона"
    assert some_grass_1.price == 500.0
    assert some_grass_1.quantity == 20
    assert some_grass_1.country == "Россия"
    assert some_grass_1.germination_period == "7 дней"
    assert some_grass_1.color == "Зеленый"

    assert some_grass_2.name == "Газонная трава 2"
    assert some_grass_2.description == "Выносливая трава"
    assert some_grass_2.price == 450.0
    assert some_grass_2.quantity == 15
    assert some_grass_2.country == "США"
    assert some_grass_2.germination_period == "5 дней"
    assert some_grass_2.color == "Темно-зеленый"


def test_lawngrass_prod_add(some_grass_1: LawnGrass, some_grass_2: LawnGrass) -> None:
    """Тестирование на сложение двух продуктов одного класса и получение их общей стоимости"""
    assert some_grass_1 + some_grass_2 == 16750.0


def test_lawngrass_prod_add_error(some_grass_1: LawnGrass) -> None:
    """Тестирование на некорректное сложение двух объектов"""
    with pytest.raises(TypeError):
        some_grass_1 + 33
