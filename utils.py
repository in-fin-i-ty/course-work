import json


def load_data(patch):
    """
    функция для чтения Json файла
    """
    with open(patch, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def filter_sort(data):
    """"
    функция для сортировки данных по дате с условием, если оперция была выполнена (EXECUTED)
    """
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data


def formatted_data(item):
    """
    функция для вывода данных в формате:
    <дата перевода> <описание перевода>
    <откуда>(если это не открытие вклада) -> <куда>
    <сумма перевода> <валюта>
    """
    item_date = format_date(item.get('date'))

    item.get('from')
    if item.get('from'):
        from_ = mask_card(item.get('from')) + " -> "
    else:
        from_ = ''

    to_ = mask_card(item.get('to'))

    return f"{item_date} {item.get('description')}\n" \
           f"{from_}{to_}\n" \
           f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n"


def format_date(str_date):
    """
    Функция для форматирования вводных данных о дате:
    ДД.ММ.ГГГГ.
    """
    list_date = str_date[0:10].split('-')
    return ".".join(reversed(list_date))


def mask_card(card):
    """
    функция для маскировки номера карты и номера счёта
    При помощи данной функции данные карты выводятся в формате: "Наименование платёжной системы" ХХХХ ХХ** **** ХХХХ
    Данные счёта будут выводиться в формате: "Счёт" **XXXX
    """
    card = card.split(" ")
    if card[0] == "Счет":
        return f"{card[0]} **{card[-1][-4:]}"
    return f'{" ".join(card[:-1])} {card[-1][: 4]} {card[-1][4: 6]}** **** {card[-1][-4:]}'