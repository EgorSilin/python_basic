"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_list = input("Введите список, разделяя значения запятой:").split(',')
changed_list = user_list.copy()
el_number = 0
for i in range(int(len(changed_list)/2)):
    changed_list[el_number], changed_list[el_number+1] = changed_list[el_number+1], changed_list[el_number]
    el_number += 2
print(f"Вы ввели лист:\n{user_list}\nЛист после перестановки элементов:\n{changed_list}")
