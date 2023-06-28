from dataclasses import dataclass

@dataclass
class Animal:
    __name: str = ""
    __age: int = 0

    def can_feed(self):
        return True

    def make_noise(self):
        return ""

    def __str__(self):
        return self.__name + ", " + "Age: " + str(self.__age)

@dataclass
class Donkey(Animal):
    def make_noise(self):
        return "hee-haw"

@dataclass
class Goat(Animal):
    def make_noise(self):
        return "maaa"
@dataclass
class HoneyBadger(Animal):
    def can_feed(self):
        return False

    def make_noise(self):
        return "rattle-grunt"

class Zoo:
    def __init__(self):
        self.__list = []

    def __iter__(self):
        for animal in self.__list:
            yield animal

    def addAnimal(self, animal):
        self.__list.append(animal)

    def __str__(self):
        return "Eric's Zoo, " + str(len(self.__list)) + " animals."




