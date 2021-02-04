
# class MyException(Exception):
#     pass
#
#
# def f():
#     raise MyException('Здесь произошло страшное')
#
# try:
#     a = f()
# except Exception as e:
#     print(e)
#
#
#
#

class TourError(Exception):
    pass


class CarBrokenError(TourError):
    pass


class SightseenIsNotAvailableError(TourError):
    pass



def move_to(place):
    raise CarBrokenError()
    print('move_to', place)


def observe(sightseen):
    print('observe', sightseen)


def eat(meal):
    print('eat', meal)


def rest():
    print('rest')


from functools import partial

activities = [
    partial(move_to, 'london'),
    partial(observe, 'Thamse'),
    partial(eat, 'tea'),
    partial(rest),
    partial(move_to, 'Paris'),
    partial(observe, 'Eiffel'),
    partial(eat, 'croasson'),
    partial(rest ),
    partial(move_to, 'home'),
    partial(eat, 'whatever you like'),
    partial(observe, 'tv'),
    partial(rest),
    partial(observe, 'tv'),
    partial(rest)
]

for activity in activities:
    try:
        activity()
    except TourError as e:
        print('Сломалась машина, Тогда поедем на поезде')
    except Exception as e:
        print(e)
        exit(1)
