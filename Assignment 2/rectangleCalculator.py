#!/usr/bin/env/python3

from rectangle import Rectangle


def getUserInput():
    while True:
        try:
            height = int(input(f"{'Height:':{'11'}}"))
            width = int(input(f"{'Width:':{'11'}}"))
            if height > 0 and width > 0:
                return height, width
            else:
                raise ValueError
        except ValueError:
            print("Please enter a positive integer. Try again.")


def main():
    print("Rectangle Calculator")
    while True:
        print()
        height, width = getUserInput()
        rectangle = Rectangle(height, width)
        print(f"{'Perimeter:':{'11'}}{rectangle.perimeter()}")
        print(f"{'Area:':{'11'}}{rectangle.area()}")
        rectangle.consoleArt()
        print()
        another = input("Continue? (y/n): ")
        if another != 'y':
            break
    print()
    print("Bye!")




if __name__ == '__main__':
    main()
