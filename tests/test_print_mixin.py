import pytest

from src.lawngrass_prod import LawnGrass
from src.product import Product
from src.smartphone_prod import Smartphone


def test_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка на вывод информации об экземплярах дочерних классов через консоль"""

    Product("Пояс тк", "Широкий, на резинке", 1000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Пояс тк, Широкий, на резинке, 1000.0, 7)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
