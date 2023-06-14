from dataclasses import dataclass
import random

class Player:

    def __init__(self, name):
        self.__name = name
        self.__value = 'r'
        self.__wins = 0

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
    @property
    def wins(self):
        return f"{self.__wins} wins."

    def setValue(self, value):
        self.__value = value

    def addWin(self):
        self.__wins += 1

    def generateRoshambo(self):
        self.__value = "r"

    def play(self, player):
        if self.value == player.value:
            return "Draw!"
        elif 'r' == self.value and 'p' == player.value:
            player.addWin()
            return f"{player.name.title()} wins!"
        elif 's' == self.value and 'r' == player.value:
            player.addWin()
            return f"{player.name.title()} wins!"
        elif 'p' == self.value and 's' == player.value:
            player.addWin()
            return f"{player.name.title()} wins!"
        else:
            self.addWin()
            return f"{self.name} wins!"

class Bart(Player):
    def __init__(self):
        Player.__init__(self, "Bart")

@dataclass
class Lisa(Player):
    def __init__(self):
        Player.__init__(self, "Lisa")

    def generateRoshambo(self):
        values = ["r", "p", "s"]
        Player.setValue(self, values[random.randint(0, 2)])

