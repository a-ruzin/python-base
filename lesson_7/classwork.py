
class A:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key == 'dddd':
            self.__dict__[key] = str(value) + 'hoho'
        else:
            self.__dict__[key] = value

x = A()
x.dddd = 333
print(x.dddd)
