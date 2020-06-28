"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from random import randint


class TrafficLight:
    def __init__(self):
        self.__color = ""

    def running(self):
        while True:
            if self.__color != "green" and self.__color != "":
                print("Ошибка в работе светофора!")
                break
            self.__color = "red"
            print(self.__color)
            sleep(7)
            if self.__color != "red":
                print("Ошибка в работе светофора!")
                break
            self.__color = "yellow"
            print(self.__color)
            sleep(2)
            if self.__color != "yellow":
                print("Ошибка в работе светофора!")
                break
            self.__color = "green"
            print(self.__color)
            sleep(randint(1, 9))

    def say_color(self):
        return self.__color


if __name__ == '__main__':
    current_light = TrafficLight()
    current_light.running()
