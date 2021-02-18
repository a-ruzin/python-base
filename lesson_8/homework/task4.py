"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Store:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else []

    def append(self, item):
        self.store.append(item)

    def remove(self, item):
        self.store.remove(item)


class OfficeEquipment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Printer(OfficeEquipment):
    def __init__(self, name, cost, max_print_size):
        super().__init__(name, cost)
        self.max_print_size = max_print_size


class Scanner(OfficeEquipment):
    def __init__(self, name, cost, media_type):
        super().__init__(name, cost)
        self.media_type = media_type


class Copier(OfficeEquipment):
    def __init__(self, name, cost, color):
        super().__init__(name, cost)
        self.color = color
