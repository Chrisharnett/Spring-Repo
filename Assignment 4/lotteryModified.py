#!/usr/bin/env/python3

import random

def lotto():
    numbers = set()
    while 6 > len(numbers):
        numbers.add(random.randint(1, 49))
    return numbers

def checkNumbers(lottoNumbers, winningNumbers):
    matches = 0
    for number in winningNumbers:
        for guess in lottoNumbers:
            if guess == number:
                matches += 1
    if 0 == matches or 1 == matches:
        return "0"
    elif 2 == matches:
        return "Free Play"
    elif 3 == matches:
        return "10"
    elif 4 == matches:
        return "90.50"
    elif 5 == matches:
        return "5000"
    elif 6 == matches:
        return "13000000"

def whatAreTheOdds(tickets, winningNumbers):
    winnings = -2 * tickets
    while 0 < tickets:
        lottoNumbers = lotto()
        prize = checkNumbers(winningNumbers, lottoNumbers)
        if "Free Play" == prize:
            tickets += 1
        else:
            winnings += float(prize)
        tickets -= 1
    return winnings
def main():
    winningNumbers = {9, 20, 27, 35, 37, 43}
    while True:
        try:
            tickets = int(input("It costs $2 to play. How many times would you like to play? (-1 to exit)  "))
            if -1 == tickets:
                break
            elif tickets > 0:
                winnings = whatAreTheOdds(tickets, winningNumbers)
                print(f"{tickets} plays leaves you  with ${winnings}.")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Enter a positive integer.")
    print()
    print("Bye!")


if __name__ == '__main__':
    main()

