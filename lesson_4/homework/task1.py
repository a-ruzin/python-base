"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def calc_salary(hours, rate, bonus):
    return hours * rate + bonus


if len(argv) != 4:
    print('Запустите программу и передайте ей параметры: выработка в часах, ставка в час, премия:')
    print(f'например: {argv[0]} 40 1000 5000')
    exit(1)

try:
    hours = float(argv[1])
    rate = float(argv[2])
    bonus = float(argv[3])
except ValueError:
    print('Все три параметра должны быть числами с плавающей точкой')
    exit(1)
else:
    salary = calc_salary(hours, rate, bonus)
    print(f'Заработная плата: {salary}')
