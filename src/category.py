from product import Product


class Category:
    """Класс для предоставления продуктов онлайн-магазина"""

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Конструктор для создания объектов класса Категория"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, product: Product):
        """Метод для добавления товаров в список продуктов категории"""
        Category.product_count += 1
        self.__products.append(product)


    @property
    def products(self):
        """Геттер для выведения информации о списке продуктов категорий в виде спец-строки"""
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product

    @property
    def product_list(self):
        """Геттер для получения списка продуктов категории"""
        return self.__products
