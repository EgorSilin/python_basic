"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import traceback


class Data:
    def __init__(self, date_par: str):
        """примает DD-MM-YYYY"""
        self.date = date_par

    @classmethod
    def class_m(cls, date_str_par):
        date_list_int = list(map(int, date_str_par.split('-')))
        return date_list_int

    @staticmethod
    def static_m(date_list_int_par: list):
        msg = ''
        if 31 < date_list_int_par[0] or date_list_int_par[0] < 1:
            msg += "День задан некорретно, допустимы значения от 1 до 31.\n"
        if 12 < date_list_int_par[1] or date_list_int_par[1] < 1:
            msg += "Месяц задан некорретно, допустимы значения от 1 до 12.\n"
        if date_list_int_par[2] < 1:
            msg += "Год задан некорретно, допустимы значения от 1.\n"
        if msg == '':
            msg += f"Дата введена верно: {'-'.join(map(str, map(lambda x: format(x, '02'), date_list_int_par)))}."
        else:
            msg += "Введите повторно с исправлениями:"
        return msg


if __name__ == '__main__':
    while True:
        user_date = input("Введите дату в формате DD-MM-YYYY (для выхода введите 'q'): ")
        if user_date == 'q':
            break
        data_obj = Data(user_date)
        try:
            print(Data.static_m(Data.class_m(user_date)))
        except ValueError as e:
            print(e, traceback.format_exc())
            print(f"Ошибка ввода! Попробуйте заново!!!")
            continue
    print("Рабо та программы завершена!")
