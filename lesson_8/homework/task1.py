"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    last_day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date_in_str):
        parts = date_in_str.split('-')
        if len(parts) != 3:
            raise ValueError('Дата должна быть в формате ДД-ММ-ГГГГ')
        self.day = int(parts[0])
        self.month = int(parts[1])
        self.year = int(parts[2])

        self.validate(self.day, self.month, self.year)

    @classmethod
    def extract(cls, date_in_str):
        date = Date(date_in_str)
        return date.day, date.month, date.year

    @staticmethod
    def validate(day, month, year):
        if not (1 <= year <= 3000):
            raise ValueError('Год должен быть в диапазоне от 1 до 3000')
        if not (1 <= month <= 12):
            raise ValueError('Месяц должен быть в диапазоне от 1 до 12')
        if not (1 <= day <= Date.last_day_in_month[month-1]):
            raise ValueError(f'День должен быть в диапазоне от 1 до {Date.last_day_in_month[month-1]}')

date = Date('28-02-2021')

print(Date.extract('28-02-2021'))
