import random
from dataclasses import dataclass


@dataclass
class Die:
    __value: int = 1
    __image: str = ""

    @property
    def value(self):
        return self.__value

    @property
    def image(self):
        if self.__value == 1:
            self.__image = (" _____ \n" +
                            "|     |\n" +
                            "|  o  |\n" +
                            "|_____|")
        elif self.__value == 2:
            self.__image = (" _____ \n" +
                            "|o    |\n" +
                            "|     |\n" +
                            "|____o|")
        elif self.__value == 3:
            self.__image = (" _____ \n" +
                            "|o    |\n" +
                            "|  o  |\n" +
                            "|____o|")
        elif self.__value == 4:
            self.__image = (" _____ \n" +
                            "|o   o|\n" +
                            "|     |\n" +
                            "|o___o|")
        elif self.__value == 5:
            self.__image = (" _____ \n" +
                            "|o   o|\n" +
                            "|  o  |\n" +
                            "|o___o|")
        elif self.__value == 6:
            self.__image = (" _____ \n" +
                            "|o   o|\n" +
                            "|o   o|\n" +
                            "|o___o|")
        return self.__image


    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die value can't be less than 1.")
        elif value > 6:
            raise ValueError("Die value can't be more than 6")
        else:
            self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value

    def __post_int__(self):
        self.__value = self.roll()



class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        return tuple(self.__list)

    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getTotal(self):
        total = 0
        for die in self.__list:
            value = die.setValue
            total += value
        return total
