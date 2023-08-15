import time
import random

def find(number, data):
    for entry in data:
        if entry == number:
            return True
    return False

def main():
    data = []
    for n in range(10000001):
        x = random.randint(1, 5000000)
        data.append(x)
    print(data[random.randint(1, 10001)])
    number = int(input("Enter an integer to find between 1 and 5000000: "))
    startStamp = time.time()
    exist = find(number, data)
    endStamp = time.time()
    print(f"Item in list? {exist}\n Time to search {endStamp - startStamp}")

if __name__ == '__main__':
    main()
