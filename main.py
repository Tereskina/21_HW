from courier import Courier
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печеньки": 25,
    "собачка": 25,
    "ёлка": 25,
    "морковь": 3,
    "телефон": 5,
    "журнал": 1
})

shop = Shop(items={
    "печеньки": 2,
    "собачка": 2,
    "ёлка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день!\n')

    while True:
        # Выводим все товары во всех хранилищах
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        # Забираем у пользователя строку с запросом
        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "stop" или "стоп", если хотите закончить\n'
        )

        if user_input in ("стоп", "stop"):
            break

        # Собираем класс запроса
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cancel()


if __name__ == '__main__':
    main()
