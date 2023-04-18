from utils import load_data, formatted_data, filter_sort

JSON_FILE = 'operations.json'


def main():
    """"
    функция для вывода 5 последних операций, отформатироанных при помощи функций из файла utils.py
    """
    data = load_data(JSON_FILE)
    data = filter_sort(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
