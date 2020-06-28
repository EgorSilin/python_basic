"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed_par: int, color_par: str, name_par: str, is_police_par: bool):
        self.speed = speed_par
        self.color = color_par
        self.name = name_par
        self.is_police = is_police_par

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction_par: str):
        print(f"Машина повернула {direction_par}.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}.")
        if self.speed > 60:
            print("Превышение скорости! Ограничение 60!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}.")
        if self.speed > 40:
            print("Превышение скорости! Ограничение 40!")


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car_obj = Car(70, 'color', 'name', False)
    print(car_obj.speed, car_obj.color, car_obj.name, car_obj.is_police)
    car_obj.go()
    car_obj.stop()
    car_obj.turn("налево")
    car_obj.show_speed()
    print('\n')

    town_car_obj = TownCar(70, 'blue', 'BMW', False)
    print(town_car_obj.speed, town_car_obj.color, town_car_obj.name, town_car_obj.is_police)
    town_car_obj.go()
    town_car_obj.stop()
    town_car_obj.turn("налево")
    town_car_obj.show_speed()
    print('\n')

    sport_car_obj = SportCar(120, 'red', 'Ferrari', False)
    print(sport_car_obj.speed, sport_car_obj.color, sport_car_obj.name, sport_car_obj.is_police)
    sport_car_obj.go()
    sport_car_obj.stop()
    sport_car_obj.turn("направо")
    sport_car_obj.show_speed()
    print('\n')

    work_car_obj = WorkCar(50, 'red', 'VW', False)
    print(work_car_obj.speed, work_car_obj.color, work_car_obj.name, work_car_obj.is_police)
    work_car_obj.go()
    work_car_obj.stop()
    work_car_obj.turn("налево")
    work_car_obj.show_speed()
    print('\n')

    police_car_obj = PoliceCar(70, 'black', 'Ford', True)
    print(police_car_obj.speed, police_car_obj.color, police_car_obj.name, police_car_obj.is_police)
    police_car_obj.go()
    police_car_obj.stop()
    police_car_obj.turn("направо")
    police_car_obj.show_speed()
    print('\n')
