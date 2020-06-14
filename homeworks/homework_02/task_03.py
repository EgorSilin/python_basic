"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

month_number = int(input("Введите номер месяца (от 1 до 12):"))

months_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if month_number in months_list[0]:
    print("Зима")
elif month_number in months_list[1]:
    print("Весна")
elif month_number in months_list[2]:
    print("Лето")
elif month_number in months_list[3]:
    print("Осень")

months_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}

for season, month in months_dict.items():
    if month_number in month:
        print(season)
