#!/usr/bin/env/python3


def printNames(players):
    playerNames = list(players.keys())
    playerNames.sort()
    print()
    print("ALL PLAYERS:")
    for player in playerNames:
        print(player)

def main():
    print("Game Stats Program")
    players = {"Paula": {"Wins": 41, "Losses": 3, "Ties": 22},
               "Miguel": {"Wins": 36, "Losses": 7, "Ties": 6},
               "Samuel": {"Wins": 107, "Losses": 2, "Ties": 78},
               "Chris": {"Wins": 13, "Losses": 3, "Ties": 43}}
    printNames(players)
    while True:
        print()
        name = input("Enter a player name: ").title()
        if name in players:
            for stats in players[name].keys():
                print(f"{stats + ':':{'9'}}{players[name][stats]}")
        else:
            print(f"There is no player named {name}")
        print()
        goOn = input("Continue? (y/n): ")
        if goOn.lower() != 'y':
            break
    print()
    print("Bye!")


if __name__ == '__main__':
    main()
