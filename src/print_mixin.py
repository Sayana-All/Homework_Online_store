class PrintMixin:
    """Класс-миксин, который при инициализации экземпляра класса выводит в консоль информацию о его нём и параметрах"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод для выведения указанной информации в консоль"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
