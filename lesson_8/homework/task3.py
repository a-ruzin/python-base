"""
3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
"""


class NotANumberError(Exception):
    pass


def get_number():
    text = input('Введите число (0 для останова):')
    if not text.isnumeric():
        raise NotANumberError
    return int(text)


number = None
result = []
while number != 0:
    try:
        number = get_number()
        result.append(number)
    except NotANumberError:
        print('это не число')

print(result)
