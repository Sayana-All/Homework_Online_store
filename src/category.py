from typing import Any, Optional

from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category:
    """Класс для предоставления категорий продуктов онлайн-магазина"""

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
        total_quantity = 0
        for prod in self.__products:
            total_quantity += prod.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> Any:
        """Метод для добавления товаров в список продуктов категории"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Товар с нулевым количеством не может быть добавлен")
            except ZeroDivisionError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен в категорию.")
            finally:
                print(f"Обработка добавления товара {product.name} завершена.")
        else:
            raise TypeError

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

    def middle_price(self) -> Any:
        """Метод для подсчета среднего ценника всех товаров категории"""
        try:
            avg_price = round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
        else:
            return avg_price
