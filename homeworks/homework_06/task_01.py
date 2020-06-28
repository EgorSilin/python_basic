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
    __color = 0

    def running(self):
        while True:
            TrafficLight.__color = "red"
            print(TrafficLight.__color)
            sleep(7)
            TrafficLight.__color = "yellow"
            print(TrafficLight.__color)
            sleep(2)
            TrafficLight.__color = "green"
            print(TrafficLight.__color)
            sleep(randint(1, 9))

    def say_color(self):
        return TrafficLight.__color


if __name__ == '__main__':
    current_light = TrafficLight()
    current_light.running()
    # print(current_light.say_color())
