#!/usr/bin/env/python3
import sys

FILENAME = "world_cup_champions.txt"

def readFile():
    winners = {}
    try:
        with open(FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                winner = line.split(',')
                if winner[1] in winners:
                    winners[winner[1]].append(winner[0])
                else:
                    winners.update({winner[1]: [winner[0]]})
        del winners['Country']
        return winners
    except FileNotFoundError as e:
        print("Could not find file.\n Exiting program. Bye!")
        sys.exit(1)
    except Exception as e:
        print("Unknown Exception, Closing Program")
        print(type(e), e)
        sys.exit(1)

def main():
    winners = readFile()
    print("FIFA World Cup Winnners")
    print()
    print(f"{'Country':{'15'}}{'Wins':{'6'}}{'Years'}")
    print(f"{'=======':{'15'}}{'====':{'6'}}{'====='}")
    winnerList = list(winners.keys())
    winnerList.sort()
    for winner in winnerList:
        years = ""
        for year in winners[winner]:
            years += year + ", "
        years = years[:-2]
        print(f"{winner:{'15'}}{len(winners[winner]):{'<6'}}{years}")


if __name__ == '__main__':
    main()
