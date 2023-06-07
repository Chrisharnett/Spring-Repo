#!/usr/bin/env/python3

# Create a simple program that when run will generate and store 10 random ints between 1 and 20 in a list
# Write a function which prompts the user for a number between 1 and 20 and checks if this number is in the list.
# If it is, output "found" otherwise output "not found"
# When searching for the number, count and then output how many comparisons are made.

import random
import time

def checkList(numberList, userNumber):
    comparisonCount = 0
    start = time.time()
    if userNumber in numberList:
        end = time.time()
        print(end-start)
        return True
    # for number in numberList:
    #     comparisonCount += 1
    #     if number == userNumber:
    #         end = time.time()
    #         print(end - start)
    #         return True, comparisonCount
    end = time.time()
    print(end-start)
    return False, comparisonCount


def getUserNumber():
    while True:
        try:
            userNumber = int(input("Enter the number to check "))
            if 1 <= userNumber <= 20000000:
                return userNumber
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid integer between 1 and 20.")


def createList():
    numberList = {}
    for i in range(5000000):
        numberList[random.randint(1, 20000000)] = True
        #numberList.append(random.randint(1, 20000000))
    return numberList


def main():
    numberList = createList()
    userNumber = getUserNumber()
    inList, comparisonCount = checkList(numberList, userNumber)
    if inList:
        print("Found")
    else:
        print("Not Found")
    print(f"Number of Comparisons: {comparisonCount}")


if __name__ == '__main__':
    main()
