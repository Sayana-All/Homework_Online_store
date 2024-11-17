from src.product import Product
from src.category import Category


class ProductIterator:
    """Класс для представления продуктового итератора в рамках одной категории"""
    def __init__(self, category_obj: Category) -> None:
        """Инициализация итератора для товаров категории"""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Создает и возвращает объект-итератор товаров категории"""
        self.index = 0
        return self

    def __next__(self):
        """Производит итерацию по товарам категории, возвращая очередной продукт"""
        if self.index < len(self.category.product_list):
            prod = self.category.product_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    iter = ProductIterator(category1)

    for i in iter:
        print(i)