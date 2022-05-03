class plusANDminus:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def state(self, a, b):
        self.first = a
        self.second = b

    def add(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

class mulANDdiv:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def multiple(self):
        return self.first * self.second

    def div(self):
        return self.first/self.second

class FourCal(plusANDminus, mulANDdiv): # 상속

    def answer(self):
        return self.add()


a = plusANDminus(4, 2)
# a.state(4, 2)
print(a.add())

b = mulANDdiv(4, 2)
print(b.multiple())

c = FourCal(4, 2)
print(c.answer())

