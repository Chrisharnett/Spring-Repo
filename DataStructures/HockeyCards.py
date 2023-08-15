#!/usr/bin/env/python3

def main():
    collection = {"Wayne Gretzky": 2, "Mario Lemieux": 3, "Sidney Crosbie": 1, "Austin Matthews": 1, "Jaromir Jagr": 2}
    extraCards = {"Wayne Gretzky": 1, "Alexander Ovechkin": 3, "Mark Messier": 2, "Bobby Hull": 1}
    cardSet = set(card for card in collection)
    for card in extraCards:
        cardSet.add(card)
    print(cardSet)
    i = 1
    for card in cardSet:
        print(f"{i}. {card}")
        i += 1


if __name__ == '__main__':
    main()
