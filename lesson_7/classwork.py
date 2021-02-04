
class MyException(Exception):
    pass


def f():
    raise MyException('Здесь произошло страшное')

try:
    a = f()
except Exception as e:
    print(e)















def move_to(place):
    pass


def observe(sightseen):
    pass


def eat(meal):
    pass


def rest():
    pass


activities = [
    move_to('london'),
    observe('Thamse'),
    eat('tea'),
    rest(),
    move_to('Paris'),
    observe('Eiffel'),
    eat('croasson'),
    rest(),
    move_to('home'),
    eat('whatever you like'),
    observe('tv'),
    rest()
]
