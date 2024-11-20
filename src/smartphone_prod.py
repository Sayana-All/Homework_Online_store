from typing import Any

from src.product import Product


class Smartphone(Product):
    """Подкласс для представления группы продуктов вида смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Конструктор для добавления новых атрибутов подкласса Смартфон"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Any:
        """Метод для сложения двух продуктов и получения их общей стоимости"""
        if type(other) is Smartphone:
            total_amount = self.price * self.quantity + other.price * other.quantity
            return total_amount
        raise TypeError
