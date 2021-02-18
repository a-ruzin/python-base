"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    pass


def div(numerator, denumerator):
    if denumerator == 0:
        raise DivisionByZero
    return numerator / denumerator

numerator = int(input('Введите числитель:'))
denumerator = int(input('Введите знаменатель:'))

try:
    result = div(numerator, denumerator)
except DivisionByZero:
    print('на ноль делить нельзя')
else:
    print(f'{numerator} / {denumerator} = {result}')
