"""
1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div(x, y):
    if y == 0:
        return 'На ноль делить нельзя'
    return x / y


nominator = float(input('Введите числитель: '))
denominator = float(input('Введите знаменатель: '))

result = my_div(nominator, denominator)
print(f'{nominator} / {denominator} = {result}')
