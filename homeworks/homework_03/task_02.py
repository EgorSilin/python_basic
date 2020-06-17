"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры, как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data_func(first_name, second_name, birth_year, current_city, email, phone_number):
    return str(f"{first_name} {second_name}, {birth_year}, {current_city}, {email}, {phone_number}")


print(user_data_func(first_name="Василий",
                     second_name="Васильев",
                     birth_year=1988,
                     current_city="Москва",
                     email="vasiliyvasilyev@gmail.com",
                     phone_number="8 999 111-22-33"))
