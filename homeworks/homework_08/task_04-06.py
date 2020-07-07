"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым (4) заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием (5).
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Stock:

    def __init__(self):
        self.item_dict_tmp = {'part_number': None, 'count': None, 'item': None}
        self.item_dict_list = []

    def show_item(self):
        """Выводит содержимое склада."""
        if not self.item_dict_list:
            print("Склад пуст!")
        else:
            for item in self.item_dict_list:
                print(item)

    def check_item(self, part_number_par):
        """Проверяет есть товар на складе."""
        for item in self.item_dict_list:
            # print(f"{item['part_number']} == {part_number_par}")#########################################
            if item['part_number'] == part_number_par:
                return True

    def take_item(self, part_number_par, count_par, item_obj):
        """Принимает товар на склад"""
        if item_obj is None:
            for item in self.item_dict_list:
                if item['part_number'] == part_number_par:
                    item['count'] = str(int(item['count']) + int(count_par))
        else:
            self.item_dict_list.append({'part_number': part_number_par, 'count': count_par, 'item': item_obj})
        print("Товар добавлен!")

    def give_item(self, part_number_par, count_par):
        """Выдает товар со склада"""
        for item in self.item_dict_list:
            if item['part_number'] == part_number_par:
                if int(item['count']) < int(count_par):
                    print(f"На складе нет достаточного количества товара. Доступно {item['count']} единиц(-ы).")
                elif int(item['count']) == int(count_par):
                    self.item_dict_list.remove(item)
                    print("Товар выдан! На складе осталось 0 единиц.")
                else:
                    item['count'] = str(int(item['count']) - int(count_par))
                    print("Товар выдан!")


class OfficeEquip:
    def __init__(self, part_number_par, prod_year_par):
        self.part_number = part_number_par
        self.prod_year = prod_year_par


class Printer(OfficeEquip):
    def __init__(self, part_number_par, prod_year_par, print_speed_par):
        super().__init__(part_number_par, prod_year_par)
        self.print_speed = print_speed_par


class Scanner(OfficeEquip):
    def __init__(self, part_number_par, prod_year_par, scan_speed_par):
        super().__init__(part_number_par, prod_year_par)
        self.scan_speed = scan_speed_par


class Xerox(OfficeEquip):
    def __init__(self, part_number_par, prod_year_par, copy_speed_par):
        super().__init__(part_number_par, prod_year_par)
        self.copy_speed = copy_speed_par


if __name__ == '__main__':
    stock_obj = Stock()
    while True:
        # stock_obj.show_item()################################################################
        data = input("Выберите действие и введите соответствующую цифру:\n"
                     "\t1 - показать содержимое склада;\n"
                     "\t2 - разместить товар на складе; \n"
                     "\t3 - выдать товар со склада; \n"
                     "\t0 - завершить работу программы.\n")
        if data == '0':
            print("Работа программы завершена!")
            break
        elif data == '1':
            stock_obj.show_item()
        elif data == '2':
            while True:
                # stock_obj.show_item()################################################################
                choice = input("Выберите действие и введите соответствующую цифру:\n"
                               "\t1 - добавить принтер;\n"
                               "\t2 - добавить сканер;\n"
                               "\t3 - добавить копировальную машину;\n"
                               "\t0 - вернуться в главное меню.\n")
                if choice == '0':
                    break
                elif choice == '1':
                    prod_year = ''
                    print_speed = ''
                    part_number = input("Введите Part Number устройства:\n")
                    if stock_obj.check_item(part_number):
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, None)
                    else:
                        print("Товар отсутствует в базе, нужно заполнить форму:\n")
                        prod_year = input("Год производства:\n")
                        print_speed = input("Скорость печати в страницах в минуту:\n")
                        print_obj = Printer(part_number, prod_year, print_speed)
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, print_obj)
                elif choice == '2':
                    prod_year = ''
                    print_speed = ''
                    part_number = input("Введите Part Number устройства:\n")
                    if stock_obj.check_item(part_number):
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, None)
                    else:
                        print("Товар отсутствует в базе, нужно заполнить форму:\n")
                        prod_year = input("Год производства:\n")
                        print_speed = input("Скорость сканирования в страницах в минуту:\n")
                        scanner_obj = Scanner(part_number, prod_year, print_speed)
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, scanner_obj)
                elif choice == '3':
                    prod_year = ''
                    print_speed = ''
                    part_number = input("Введите Part Number устройства:\n")
                    if stock_obj.check_item(part_number):
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, None)
                    else:
                        print("Товар отсутствует в базе, нужно заполнить форму:\n")
                        prod_year = input("Год производства:\n")
                        print_speed = input("Скорость копирования в страницах в минуту:\n")
                        xerox_obj = Xerox(part_number, prod_year, print_speed)
                        count = input("Введите количество единиц для помещения на склад:\n")
                        stock_obj.take_item(part_number, count, xerox_obj)
        elif data == '3':
            part_number = input("Введите Part Number устройства:\n")
            if stock_obj.check_item(part_number):
                count = input("Введите количество единиц для выдачи со склада:\n")
                stock_obj.give_item(part_number, count)
            else:
                print("Данного товара нет на складе!")
