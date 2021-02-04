
class Wheel:
    def __init__(self, radius, width):
        self.radius = radius
        self.width = width

    def __iadd__(self, other):
        if self.radius == other.radius:
            self.width += other.width
        else:
            raise Exception('Два колеса разных радиусов нельзя скрепить')
        return self



x = Wheel(12, 200)
y = Wheel(12, 100)

x += y

print(x.width)
