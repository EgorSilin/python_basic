"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name: str):
        self.__name = name

    def __add__(self, other):
        return round(self.calc_tissue_cons() + other.calc_tissue_cons(), 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @abstractmethod
    def calc_tissue_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def calc_tissue_cons(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.height = height

    def calc_tissue_cons(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    def print_result():
        print(f"Для пошива пальто {coat_obj.name} размера {coat_obj.size} "
              f"нужно {coat_obj.calc_tissue_cons()} ткани.\n"
              f"Для пошива костюма {suit_obj.name} ростовки {suit_obj.height} "
              f"нужно {suit_obj.calc_tissue_cons()} ткани.\n"
              f"В общем для пошива нужно {coat_obj + suit_obj} ткани.\n")


    coat_obj = Coat("Toto Group", 10)
    suit_obj = Suit("Henderson", 10)
    print_result()
    coat_obj.name, coat_obj.size, suit_obj.name, suit_obj.height = "New Coat Name", 20, "New Suit Name", 20
    print_result()
