"""1. Реализовать скрипт,
в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary_calc(working_hours_count_arg: float, payment_per_hour_arg: float, bonus_arg: float):
    """(working_hours_count_arg * payment_per_hour_arg) + bonus_arg -> salary

    :param working_hours_count_arg: float
    :param payment_per_hour_arg: float
    :param bonus_arg: float
    :return: salary: float
    """
    salary = (working_hours_count_arg * payment_per_hour_arg) + bonus_arg
    return salary


if __name__ == "__main__":
    _, working_hours_count_par, payment_per_hour_par, bonus_par = argv
    print(salary_calc(float(working_hours_count_par), float(payment_per_hour_par), float(bonus_par)))
