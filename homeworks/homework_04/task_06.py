"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from sys import argv
from itertools import count
from itertools import cycle


def script_a(arg_1, arg_2):
    """Выводит список целых чисел начинающийся с arg_1 и заканчивающийся arg_2"""
    for el in count(int(arg_1)):
        if el > int(arg_2):
            break
        else:
            print(el)


def script_b(arg_1):
    """Выводит элементы списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] в цикле arg_1 раз"""
    def_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    i = 0
    for el in cycle(def_list):
        if i >= int(arg_1):
            break
        print(el)
        i += 1


if __name__ == "__main__":
    script_menu = {'a': script_a,
                   'b': script_b}
    _, script, *any_arg = argv
    script_menu[script](*any_arg[:])
