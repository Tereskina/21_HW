from base_storage import BaseStorage
from exceptions import TooManyDifferentProducts


class Shop(BaseStorage):
    # Shop не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров.
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(name, amount)
