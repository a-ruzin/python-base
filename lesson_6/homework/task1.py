"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import time


class Mode:
    def __init__(self, color, delay):
        self.color = color
        self.delay = delay


class TrafficLight:
    modes = [
        Mode('red', 7),
        Mode('yellow', 2),
        Mode('green', 3),
    ]

    def __init__(self):
        self.index = 0

    def switch(self):
        mode = self.modes[self.index]
        time.sleep(mode.delay)
        self._switch_to_next()
        mode = self.modes[self.index]
        return mode.color

    def _switch_to_next(self):
        self.index += 1
        self.index %= len(self.modes)


light = TrafficLight()

inital_time = time.time()

for i in range(10):
    color = light.switch()
    elapsed = int(time.time()-inital_time)
    print(elapsed, color)
