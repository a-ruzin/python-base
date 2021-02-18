# # ООП
#
# # print(type(3))
# # print(type('asdf'))
# # print(type([]))
#
#
# # Фамилия зарплата Руководитель
# #
# # Иванов 30000 Сидоров
#
# manager = {
#     'name': 'Иванов',
#     'salary': 30000,
#     'boss': 'Сидоров'
# }
# employee1 = dict(manager)
#
# employee1['sadary'] = 490999
#
# employee2 = dict(manager)
# employee3 = dict(manager)
#
# employees = [
#     manager,
#     employee1,
#     employee2,
#     employee3,
# ]
#
#
#
# class Employee:
#
#     def __init__(self, name, salary=0):
#         self.salary = salary
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name} ({self.salary})'
#
#     def raise_salary(self, amount):
#         self.salary += amount
#
#     def dump(self):
#         return 1
#
#
# class Manager(Employee):
#     _subordinates = []
#     birth_year = None
#     _cache = {}
#
#     def __init__(self, name, salary, birth_year):
#         super().__init__(name, salary)
#         self.birth_year = birth_year
#         self._cache[name] = salary
#
#     def __str__(self):
#         return f'!{self.name} ({self.salary}), подчиненные: {len(self._subordinates)}'
#
#     def add_employee(self, employee):
#         self._subordinates.append(employee)
#         self._cache[employee.name] = employee.salary
#
#     def raise_salary_for_all_subordinates(self, amount):
#         for employee in self._subordinates:
#             employee.raise_salary(amount)
#
#     def dump(self):
#         return 2
#
# manager = Manager('Иванов', 100000, 1990)
# manager.raise_salary(8888)
#
# employee = Employee('Сидоров', 50000)
#
# manager.add_employee(employee)
# print([str(x) for x in manager._subordinates])
# # print(employee, manager)
# # manager.raise_salary_for_all_subordinates(15000)
# # print(employee, manager)
#
# all_employees = [
#     employee,
#     manager,
#     employee,
#     manager
# ]
#
#
# for emp in all_employees:
#     print(emp.dump())
#
#
#
# xxx = SuperClass(1,2,3, {'wage': 1000, 'bonus': 200})
#
#
# # Инкапсуляция
#
# # Наследование
#
# # Полиморфизм
#
# # абстракция -- ??


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def input(self):
        pass


class B(A):
    def print(self):
        print('Я метод adfzsdf в производном классе')


class C(B):
    def input(self):
        x = input('Я метод input в производном классе')
        return x


c = C()
c.print()
value = c.input()
print('вы ввели', value)
