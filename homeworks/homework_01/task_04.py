"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("Введите число: "))
number_counter = number
numeral_max = 0

while number_counter > 1:
    remainder = number_counter % 10
    number_counter = number_counter // 10
    if remainder > numeral_max:
        numeral_max = remainder
print(f"В числе {number} самая большая цифра {numeral_max}")