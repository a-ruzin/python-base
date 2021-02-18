"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from functools import partial
from random import randint, choice


class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print(f'{self.color} {self.name} едет')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'{self.color} {self.name} остановился')

    def turn(self, where):
        if self.speed != 0:
            print(f'{self.color} {self.name} повернул {where}')
            self.show_speed()
        else:
            print(f'{self.color} {self.name} стоит')

    def show_speed(self):
        print(f' скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(' Превышение!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(' Превышение!')


class PoliceCar(Car):
    pass


cars = [
    TownCar('черный', 'BMW', False),
    SportCar('зеленый', 'Porshe', False),
    WorkCar('белая', 'Газель', False),
    PoliceCar('белая', 'Лада', True),
]

for i in range(10):
    for car in cars:
        methods = [
            partial(car.stop),
            partial(car.go, randint(10, 100)),
            partial(car.turn, choice(['Север', 'Запад', 'Юг', 'Восток'])),
        ]
        choice(methods)()
        print()
