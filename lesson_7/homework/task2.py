"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
 параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def get_material_size(self):
        pass

    @property
    def size(self):
        return self.get_material_size()


class Suit(Cloth):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_material_size(self):
        return self.w * self.h


class Coat(Cloth):
    def __init__(self, s, length):
        self.s = s
        self.length = length

    def get_material_size(self):
        return self.s * self.length * 2


suit = Suit(10, 5)
coat = Coat(5, 3)

clothes = [suit, coat]
for cloth in clothes:
    print(cloth.size)
