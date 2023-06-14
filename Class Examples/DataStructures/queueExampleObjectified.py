#!/usr/bin/env/python3

from queueObject import Queue
def main():
    queue = Queue()
    print("Welcome to the store")
    print()
    while True:
        print("1 - Get in line")
        print("2 - Process customer")
        choice = int(input("What would you like to do? "))
        if 1 == choice:
            queue.enqueue()
        elif 2 == choice:
            try:
                queue.dequeue()
            except IndexError as e:
                print(e)
        choice = input("Continue (y/n): ")
        if "y" != choice.lower():
            break


if __name__ == '__main__':
    main()
