#!/usr/bin/env/python3

import random
from datetime import datetime, timedelta
import csv
import sys

LOWVALUE = 10000
HIGHVALUE = 200000
INTERVAL = 10000


def output(results, algo):
    filename = algo + ".csv"
    try:
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow([algo])
            writer.writerow(["Number of elements", "Average Time in 10 sorts"])
            for key, value in results.items():
                writer.writerow([key, value])
    except Exception as e:
        print("Unknown error, closing program.\n")
        print(type(e), e)
        sys.exit(1)


#  copied from https://www.geeksforgeeks.org/python-program-for-quicksort/
def quickSort(values):
    if len(values) <= 1:
        return values
    else:
        pivot = values[0]
        left = [x for x in values[1:] if x < pivot]
        right = [x for x in values[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)


# copied from https://www.geeksforgeeks.org/python-program-for-heap-sort/
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        # Heapify the root.

        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# This code is contributed by Mohit Kumra


# copied from https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of MergeSort

def mergeSort(values):
    if len(values) > 1:

        # Finding the mid of the array
        mid = len(values) // 2

        # Dividing the array elements
        L = values[:mid]

        # Into 2 halves
        R = values[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                values[k] = L[i]
                i += 1
            else:
                values[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            values[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            values[k] = R[j]
            j += 1
            k += 1

# This code is contributed by Mayank Khanna


def bubbleSort(values):
    for passNumber in range(len(values) - 1):
        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                temp = values[index]
                values[index] = values[index + 1]
                values[index + 1] = temp

def main():
    algo = ""
    results = {}
    for n in range(LOWVALUE, HIGHVALUE + 1, INTERVAL):
        data = []
        times = []
        # Run sort code 10 times
        for p in range(5):
            for o in range(n):
                data.append(random.randint(1, HIGHVALUE))
            startStamp = datetime.now()
            mergeSort(data)
            algo = "mergesort"
            # quickSort(data)
            # algo = "quicksort"
            # heapSort(data)
            # algo = "heapSort"
            # bubbleSort(data)
            # algo = "bubble"
            endStamp = datetime.now()
            sortTime = endStamp - startStamp
            times.append(sortTime)
        total = timedelta(0)
        # get average over 10 times.
        for time in times:
            total = total + time
        avgSpeed = total / len(times)
        timeValue = f"{avgSpeed.total_seconds()}"
        results.update({n: timeValue})
    output(results, algo)


if __name__ == '__main__':
    main()
