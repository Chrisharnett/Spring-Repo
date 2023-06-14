import random

class RandomIntList(list):
    def __init__(self, n):
        list.__init__(self)
        for i in range(n):
            self.append(random.randint(1, 100))

    def numberCount(self):
        return len(self)

    def total(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self)

    def __str__(self):
        string = ""
        for n in self:
            string += f"{n}, "
        return string.removesuffix(", ")


