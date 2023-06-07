#!/usr/bin/env/python3

from cards import *

def main():
    print("Card Dealer")
    print()
    deck = Deck()
    deck.shuffleDeck()
    print(f"I have shuffled a deck of {deck.cardsInDeck()} cards")
    print()
    n = int(input("How many cards would you like?: "))
    print("Here are your cards")
    for i in range(n):
        card = deck.deal()
        print(card.cardString())
    print()
    print(f"There are {deck.cardsInDeck()} cards left in the deck.")
    print()
    print("Good luck!")


if __name__ == '__main__':
    main()
