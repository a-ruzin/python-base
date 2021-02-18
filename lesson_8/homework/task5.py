"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


class Store:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else []

    def append(self, item):
        self.store.append(item)
        item.place = 'store'

    def move(self, item, department):
        self.store.remove(item)
        item.place = department


class OfficeEquipment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.place = None


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


store = Store()
item = Printer('hp1320', 5000, 'A4')

store.append(item)

print(item.name, item.place)
store.move(item, 'Продажи')
print(item.name, item.place)
