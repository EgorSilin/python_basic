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
    item_dict = {'name': None, 'count': None, 'weight': None}
    item_dict_list = []

    def take_item(self, item_dict):
        self.item_dict_list.append(item_dict)

    def give_item(self):
        pass


class OfficeEquip:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Printer(OfficeEquip):
    def __init__(self, name, count, print_speed):
        super().__init__(name, count)
        self.print_speed = print_speed


class Scanner(OfficeEquip):
    def __init__(self, name, count, scan_speed):
        super().__init__(name, count)
        self.scan_speed = scan_speed


class Xerox(OfficeEquip):
    def __init__(self, name, count, copy_speed):
        super().__init__(name, count)
        self.copy_speed = copy_speed


if __name__ == '__main__':
    pass
