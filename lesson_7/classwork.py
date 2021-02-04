
class A:
    def __init__(self, xxx):
        self.xxx = xxx

    def __getitem__(self, index):
        return self.xxx[-index]


x = A('asdfasdf')
print(x[2])
