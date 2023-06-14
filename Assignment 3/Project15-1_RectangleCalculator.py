#!/usr/bin/env/python3

from objects import *

def rectangleInput():
    while True:
        try:
            height = int(input(f"{'Height:':{'11'}}"))
            width = int(input(f"{'Width:':{'11'}}"))
            if height > 0 and width > 0:
                return Rectangle(height, width)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a positive integer. Try again.")
def squareInput():
    while True:
        try:
            sideLength = int(input(f"{'Length:':{'11'}}"))
            if sideLength > 0:
                return Square(sideLength)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a positive integer. Try again.")


def main():
    print("Rectangle Calculator")
    while True:
        print()
        shape = input("Rectangle or square? (r/s): ")
        if "r" == shape.lower():
            shape = rectangleInput()
        elif "s" == shape.lower():
            shape = squareInput()
        print(f"{'Perimeter:':{'11'}}{shape.perimeter()}")
        print(f"{'Area:':{'11'}}{shape.area()}")
        print(shape.__str__())
        print()
        another = input("Continue? (y/n): ")
        if another != 'y':
            break
    print()
    print("Bye!")


if __name__ == '__main__':
    main()
