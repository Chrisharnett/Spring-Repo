import random

def bubbleSort(values):
    for passNumber in range(len(values) - 1):
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                temp = values[index]
                values[index] = values[index+1]
                values[index+1] = temp

def main():
    data = []
    for n in range(10000):
        data.append(random.randint(1, 10000))
        bubbleSort(data)
    # data = [45, 875, 2, 976, 2, 5, 7, 3, 42568, 456, 23, 34]
    # bubbleSort(data)
    print(data)

if __name__ == '__main__':
    main()

