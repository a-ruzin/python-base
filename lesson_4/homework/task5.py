"""
5. Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""


from functools import reduce


def mul(x, y):
    return x * y


result = reduce(mul, range(100, 1001, 2))
print(result)


# альтернативный способ
import operator

result = reduce(operator.mul, range(100, 1001, 2))
print(result)
