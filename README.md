<h1 align="center">Привет, меня зовут Александр!</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h2 align="center">Я студент онлайн университета Skypro по профессия Python-разработчик IND</h2>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" height="200"/></2>

Хочу ознакомить вас с моей курсовой работой по курсу "Основы backend-разработки"

Задача курсовой работы была в том, чтобы реализовать функцию которая выводит 5 последних(по дате) выполненных операция клиентом банка в формате:

<дата перевода> <описание перевода>

<откуда> -> <куда>

<сумма перевода> <валюта>

Где дата перевода должна быть выведена в формате: ДД.ММ.ГГГГ

Номре карты отображается в формате: XXXX XX** **** XXXX

Номер счёта отображается в формате: **XXXX

Данные по операциям были предоставлены в формате [Json фала.](https://github.com/in-fin-i-ty/course-work/blob/main/operations.json)

В файле [main.py](https://github.com/in-fin-i-ty/course-work/blob/main/main.py) лежит функция для вывода 5 последних операция на основе функций форматирования данных из файла [utils.py](https://github.com/in-fin-i-ty/course-work/blob/main/utils.py).

Так же при помощи Pytest были написаны [тесты](https://github.com/in-fin-i-ty/course-work/blob/main/tests/test_utils.py) к функциям проекта с покрытием в 100%.
