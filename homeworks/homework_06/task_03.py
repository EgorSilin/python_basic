"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name_par, surname_par, position_par, wage_par, bonus_par):
        self.name = name_par
        self.surname = surname_par
        self.position = position_par
        self._income = {"wage": wage_par, "bonus": bonus_par}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    @property
    def get_inc(self):
        return self._income


if __name__ == '__main__':
    position_obj = Position("Ivan", "Ivanov", "Engineer", 20, 50)
    print(f"Check Attributes: {position_obj.name, position_obj.surname, position_obj.position, position_obj.get_inc}")
    print(f"Full Name: {position_obj.get_full_name()}")
    print(f"Total Income: {position_obj.get_total_income()}")
