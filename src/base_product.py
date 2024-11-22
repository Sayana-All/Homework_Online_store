from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления шаблона будущих подклассов продукта"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> None:
        """Абстрактный метод для создания шаблона атрибутов продуктов"""
        pass
