#!/usr/bin/env//python3
from objects import Queue

def stutter(queue):
    stutterQueue = Queue()
    while queue.hasItems():
        value = queue.dequeue()
        for i in range(2):
            stutterQueue.enqueue(value)
    return stutterQueue

def main():
    numbers = Queue()
    userInput = input("Enter a series of numbers: ")
    for number in userInput:
        numbers.enqueue(number)
    stutterQueue = stutter(numbers)
    while stutterQueue.hasItems():
        print(stutterQueue.dequeue())









if __name__ == '__main__':
    main()