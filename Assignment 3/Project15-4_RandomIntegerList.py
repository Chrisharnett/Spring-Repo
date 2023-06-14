#!/use/bin/env/python3

from RandomIntList import RandomIntList

def printList(randomIntList):
    col = '8'
    print("Random Integers")
    print("===============")
    print(f"{'Integers: ':{col}}{randomIntList.__str__()}")
    print(f"{'Count: ':{col}}{randomIntList.numberCount()}")
    print(f"{'Total: ':{col}}{randomIntList.total()}")
    print(f"{'Average: ':{col}}{randomIntList.average():.3f}")
    print()

def main():
    print("Random Integer List")
    print()
    while True:
        try:
            n = int(input("How many random integers should the list contain?: "))
            if n <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a valid positive integer, try again.")
    print()
    while True:
        randomIntList = RandomIntList(n)
        printList(randomIntList)
        choice = input("Continue? (y/n)")
        print()
        if "y" != choice:
            break
    print("Bye!")


if __name__ == '__main__':
    main()

