# map

v = map(str, range(10))
print(v)
print(type(v))
print(list(v))


# FUNCTOOLS -------------------
#
# from functools import reduce, partial
# #
# # reduce()
#
# print(reduce(lambda acc, x: acc+x, range(1, 10)))



# partial()

# def power(x, y):
#     return x ** y
#
# square = partial(power, y=2)
# print(square(2))
# print(square(3))
#
#
# cube = partial(power, y=3)
# print(cube(2))
# print(cube(3))




# ВСПОМНИМ про генераторы

def gen(x):
    for y in range(x):
        yield y*y

for i in gen(10):
    print(i)

g = gen(10)
print(g, type(g))

# ITERTOOLS -------------------

# from itertools import repeat, cycle, islice, chain, filterfalse
