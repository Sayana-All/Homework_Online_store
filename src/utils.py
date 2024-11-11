import json
import os

from src.category import Category
from src.product import Product


def read_file_json(file_path: str) -> list[dict]:
    """Функция чтения данных из JSON-файла"""
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_file(data: list[dict]) -> list:
    """Функция создания экземпляров класса из данных файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    result = read_file_json(r"data\products.json")
    obj = create_objects_from_file(result)

    print(obj[0].name)
    print(obj[1].products)
    print(obj[0].category_count)
