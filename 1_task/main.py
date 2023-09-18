"""
Вам поручили написать простой парсер для значений, которые вы получаете из внешнего API.
На вход вы получаете список строк, в которых нечетные слова - это ключи, а четные слова - это их значения.
Ключи, значения которых вы должны учитывать - id, name, last_name, age, salary, position. Остальные ключи и их значения
не должны попасть в итоговый набор данных.
Ключ age и id должен быть представлен в формате int.
Ключ salary должен быть представлен в формате Decimal.

Ограничения:
1) На вход подается информация по сотрудникам, где всегда четное количество слов
2) Там, где нужны числовые значения, числа могут быть преобразованы к int или Decimal без ошибок.

После парсинга вы должны получить структуру данных, описанную ниже list[dict[str, int | str]]:
[
    {'id': 1, 'name': 'Ivan', 'last_name': 'Ivanov', 'age': 29, 'position': developer, 'salary': Decimal('10000')},
    ...
]

для тестирования запустить pytest 1_task/test.py
"""

import os
from decimal import Decimal


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    employees_info = get_employees_info()
    parsed_employees_info = []

    keys_to_keep = ['id', 'name', 'last_name', 'age', 'salary', 'position']
    keys_to_int = ['id', 'age']
    keys_to_decimal = ['salary']

    for employee in employees_info:
        employee_features = employee.split()
        filtered_dict = {}

        for i in range(0, len(employee_features), 2):
            key, value = employee_features[i], employee_features[i + 1]
            if key in keys_to_keep:
                try:
                    if key in keys_to_int:
                        filtered_dict[key] = int(value)
                    elif key in keys_to_decimal:
                        filtered_dict[key] = Decimal(value)
                    else:
                        filtered_dict[key] = value
                except ValueError:
                    print(f"Ошибка преобразования '{value}' ключа '{key}' в нужный тип")

        parsed_employees_info.append(filtered_dict)

    return parsed_employees_info
