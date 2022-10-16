from base_storage import BaseStorage


class Store(BaseStorage):
    # Склад Store не может быть заполнен если свободное место закончилось
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)
