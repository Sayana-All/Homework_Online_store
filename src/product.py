from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для предоставления продуктов онлайн-магазина"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор для создания объектов класса Продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Отображение класса Product для пользователей"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Метод для сложения двух продуктов и получения их общей стоимости"""
        if type(other) is Product:
            total_amount = self.__price * self.quantity + other.__price * other.quantity
            return total_amount
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict[str, Any]) -> Any:
        """Класс-метод, принимающий параметры товара в словаре и возвращающий объекты класса Product"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для изменения цены продукта"""
        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_answer = input(
                    "Новая цена товара ниже старой. Вы уверены, что хотите изменить цену?\nВведите 'y'/'n' (yes/no): "
                )
                if user_answer == "y":
                    self.__price = new_price
