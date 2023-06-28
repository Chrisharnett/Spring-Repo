#!/usr/bin/env/python3

import random
from objects import Stack

def reverse(numberList):
    stack = Stack()
    for number in numberList:
        stack.push(number)
    reverseList = []
    while 0 < stack.length():
        reverseList.append(stack.pop())
    return reverseList
def main():
    numberList = []
    for i in range(random.randint(1, 10)):
        numberList.append(random.randint(1, 1000))
    numberString = "Forward: "
    for number in numberList:
        numberString += f"{number}, "
    print(numberString.removesuffix(", "))
    reverseList = reverse(numberList)
    reverseString = "Reverse: "
    for number in reverseList:
        reverseString += f"{number}, "
    print(reverseString.removesuffix(", "))

if __name__ == '__main__':
    main()
