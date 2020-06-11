"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number_single = input("Введите число: ")
number_double = number_single * 2
number_triple = number_single * 3
number_sum = int(number_single) + int(number_double) + int(number_triple)
print(f"Вы ввели число 3 {number_single}, для которого:\nn + nn + nnn = "
      f"{number_single} + {number_double} + {number_triple} = {number_sum}.")

