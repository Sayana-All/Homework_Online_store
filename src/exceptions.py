class ZeroQuantityProduct(Exception):
    """Класс исключения при добавлении в категорию товара с нулевым количеством"""

    def __init__(self, message=None) -> None:
        """Конструктор класса исключения"""
        super().__init__(message)
