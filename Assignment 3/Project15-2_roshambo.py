#!/usr/bin/env/python3

from roshamboObjects import *

def getOpponent():
    opponent = input("Would you like to play Bart or Lisa? (b/l): ")
    if "b" == opponent.lower():
        return Bart()
    elif "l" == opponent.lower():
        return Lisa()
def roshamboString(roshambo):
    if "r" == roshambo:
        return "rock"
    elif "s" == roshambo:
        return "scissors"
    elif "p" == roshambo:
        return "paper"

def main():
    print("Roshambo Game")
    print()
    player = Player(input("Enter your name: "))
    print()
    opponent = getOpponent()
    print()
    while True:
        player.setValue(input("Rock, paper or scissors? (r/p/s): "))
        print()
        print(f"{player.name.title() + ':':{'10'}}{roshamboString(player.value)}")
        opponent.generateRoshambo()
        print(f"{opponent.name + ':':{'10'}}{roshamboString(opponent.value)}")
        print(opponent.play(player))
        print()
        print(f"{player.name.title() + ':':{'10'}}{player.wins}")
        print(f"{opponent.name + ':':{'10'}}{opponent.wins}")
        print()
        playAgain = input("Play again? (y/n): ")
        if "y" != playAgain.lower():
            break
    print()
    print("Thanks for Playing!")


if __name__ == '__main__':
    main()
