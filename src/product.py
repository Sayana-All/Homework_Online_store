class Product:
    """Класс для предоставления продуктов онлайн-магазина"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Конструктор для создания объектов класса Продукт"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
