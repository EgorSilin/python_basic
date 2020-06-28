"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра. """


class Stationery:
    def __init__(self):
        self.title = 'title'

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'pen'

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'pencil'

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Handle'

    def draw(self):
        print("Запуск отрисовки маркером.")


stationary_obj = Stationery()
print(stationary_obj.title)
stationary_obj.draw()

pen_obj = Pen()
print(pen_obj.title)
pen_obj.draw()

pencil_obj = Pencil()
print(pencil_obj.title)
pencil_obj.draw()

handle_obj = Handle()
print(handle_obj.title)
handle_obj.draw()
