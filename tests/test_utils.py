from utils import filter_sort, load_data, format_date, mask_card, formatted_data


def test_load_data():
    list_ = [
        {"id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         "operationAmount": {
             "amount": "31957.58",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"
         }
    ]
    assert load_data('test.json') == list_


def test_filter_sort():
    list_ = [
        {'id': 1,
         'state': 'EXECUTED',
         'date': '2018-08-14T05:42:30.104666'
         },
        {'id': 2,
         'state': 'Open',
         'date': '2019-08-14T05:42:30.104666'
         },
        {'id': 3,
         'state': 'EXECUTED',
         'date': '2020-08-14T05:42:30.104666'
         }
    ]
    sorted_list = [
        {'id': 3,
         'state': 'EXECUTED',
         'date': '2020-08-14T05:42:30.104666'
         },
        {'id': 1,
         'state': 'EXECUTED',
         'date': '2018-08-14T05:42:30.104666'
         }
    ]

    assert filter_sort(list_) == sorted_list


def test_format_date():
    assert format_date('2019-03-23T01:09:46.296404') == '23.03.2019'
    assert format_date('2018-09-12T21:27:25.241689') == '12.09.2018'


def test_mask_card():
    assert mask_card("Счет 27248529432547658655") == "Счет **8655"
    assert mask_card("Visa Gold 7305799447374042") == "Visa Gold 7305 79** **** 4042"
    assert mask_card("MasterCard 4956649687637418") == "MasterCard 4956 64** **** 7418"


def test_formatted_data():
    dict1 = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    dict2 = {
        "id": 801684332,
        "state": "EXECUTED",
        "date": "2019-11-05T12:04:13.781725",
        "operationAmount": {
            "amount": "21344.35",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 77613226829885488381"
    }
    str1 = '26.08.2019 Перевод организации\n' \
           'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
           '31957.58 руб.\n'
    str2 = '05.11.2019 Открытие вклада\n' \
           'Счет **8381\n' \
           '21344.35 руб.\n'
    assert formatted_data(dict1) == str1
    assert formatted_data(dict2) == str2
