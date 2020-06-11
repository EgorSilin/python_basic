"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды,
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

seconds = int(input("Введите количество секунд: "))
hours_full = seconds // 3600
minutes_full = (seconds % 3600) // 60
seconds_full = (seconds % 3600) % 60
print(f"{seconds} секунд равно {hours_full:02}:{minutes_full:02}:{seconds_full:02}.")
