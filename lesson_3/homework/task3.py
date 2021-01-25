"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_two_greatest(a, b, c):
    two_greatest = sorted([a, b, c], reverse=True)[:2]
    return sum(two_greatest)
    # return two_greatest[0] + two_greatest[1]


x = int(input('Введите первое целое число: '))
y = int(input('Введите второе целое число: '))
z = int(input('Введите третье целое число: '))

result = sum_two_greatest(x, y, z)
print(f'Сумма двух наибольших чисел: {result}')
