"""
Необычная сортировка списка

a = [1,2,3,4,5,6,6,5,4,3,2,1]

1,3,5,5,2,4,4,2
"""


a = 33


def f(b, a):
    c = 77

    a = 55
    print('f:', a, b, c)

    def g(a,b,c):
        c = 88
        print('g:', a, b, c)

    print('before c:', c)
    g()
    print('after c:', c)

a = f(44, a)
print(a)
