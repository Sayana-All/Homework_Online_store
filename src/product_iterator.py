from typing import Any, Iterator

from src.category import Category


class ProductIterator:
    """Класс для представления продуктового итератора в рамках одной категории"""

    def __init__(self, category_obj: Category) -> None:
        """Инициализация итератора для товаров категории"""
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Any:
        """Создает и возвращает объект-итератор товаров категории"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Производит итерацию по товарам категории, возвращая очередной продукт"""
        if self.index < len(self.category.product_list):
            prod = self.category.product_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration
