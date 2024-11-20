from typing import Any

from src.product import Product


class LawnGrass(Product):
    """Подкласс для представления группы продуктов вида газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Конструктор для добавления новых атрибутов подкласса Газонная трава"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        """Метод для сложения двух продуктов и получения их общей стоимости"""
        if type(other) is LawnGrass:
            total_amount = self.price * self.quantity + other.price * other.quantity
            return total_amount
        raise TypeError
