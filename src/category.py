from typing import Optional, Any

from src.product import Product


class Category:
    """Класс для предоставления продуктов онлайн-магазина"""

    name: str
    description: str
    products: list[Any]
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: Optional[list[Any]] = None) -> None:
        """Конструктор для создания объектов класса Категория"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self) -> str:
        """Отображение класса Category для пользователей"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в список продуктов категории"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для выведения информации о списке продуктов категорий в виде спец-строки"""
        str_product = ""
        for product in self.__products:
            str_product += f"{str(product)}\n"
        return str_product

    @property
    def product_list(self) -> list[Any]:
        """Геттер для получения списка продуктов категории"""
        return self.__products
