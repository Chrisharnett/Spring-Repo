from dataclasses import dataclass
from random import shuffle

@dataclass
class Card:
    __rank: str = "A"
    __suit: str = "\u2663"

    def cardString(self):
        return f"{self.__rank:{'2'}} of {self.__suit}"

class Deck:

    def __init__(self):
        suits = ["\u2663", "\u2660", "\u2661", "\u2662"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                deck.append(card)
        self.__list = deck

    @property
    def list(self):
        return tuple(self.__list)

    def shuffleDeck(self):
        return shuffle(self.__list)

    def cardsInDeck(self):
        return len(self.__list)

    def deal(self):
        return self.__list.pop()








