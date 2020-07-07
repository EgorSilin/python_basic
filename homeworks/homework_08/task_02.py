"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivByZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    dividend = float(input("Введите делимое: "))
    try:
        divider = float(input("Введите делитель: "))
        if divider == 0:
            raise DivByZeroErr("Делить на ноль нельзя!")
    except DivByZeroErr as er:
        print(er)
    else:
        print(f"Все хорошо. Частное равно: {dividend / divider}")
