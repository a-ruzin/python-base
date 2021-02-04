
class A:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'!{self.a}!'

    def __add__(self, other):
        if hasattr(other, 'a'):
            return A(self.a + other.a)
        else:
            return A(self.a + other)

x = A(3)
y = A(15)
print(x, y)

z = x + y
v = x + 'asdf'

print(z, v)
