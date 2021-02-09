"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Рисую {self.title} ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Рисую {self.title} карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Рисую {self.title} маркером')


stats = [
    Pen('Зеленой'),
    Pencil('Простым'),
    Handle('Красным')
]

for stat in stats:
    stat.draw()
