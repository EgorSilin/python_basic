"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from random import randint
from functools import reduce


def calc_func(prev_el, el):
    return prev_el * el


gen_list = [randint(100, 1000) for el in range(0, 4)]
print(gen_list)
print(reduce(calc_func, gen_list))
