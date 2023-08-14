#!/user/bin/env/python3

def bubbleSort(values):
    for passNumber in range(len(values) - 1):
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                temp = values[index]
                values[index] = values[index + 1]
                values[index + 1] = temp

def main():
    inputArray = [21, 6, 9, 33, 3]
    bubbleSort(inputArray)
    print(inputArray)

if __name__ == '__main__':
    main()

# Bubblesort is a simple sorting algorithm.
# Because each item must be accessed and iterated over, it has a time complexity of O(n2),
# making it, generally, quite inefficient in the real world.
# It does have the advantage of not requiring additional space to implement,
# as the iterates over the list in-place. As a result the space complexity is described as O(1).
# Bubblesort does perform very well in lists that are close to sorted order,
# so providing data that is already close to sorted is one way to optimize the bubblesort algorithm.
