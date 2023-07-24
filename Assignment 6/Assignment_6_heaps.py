#!/usr/bin/env/python3

import random
import heapq
import time

class Customer:
    def __init__(self, priority, custId, name):
        self.__priority = priority
        self.__id = custId
        self.__name = name

    def getPriority(self):
        return self.__priority

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
def names():
    name = ["paula", "kieran", "steve", "jojo", "michael",
            "susan", "sam", "leslie", "patrick", "tim",
            "jason", "peter", "justin", "allison", "anna",
            "mary beth", "romesh", "theresa", "morgan", "chris"]
    return name[random.randint(0, 19)]

def main():
    # Part A
    values = []
    for i in range(100):
        values.append(random.randint(1, 500))
    heapq.heapify(values)
    while len(values) > 0:
        val = heapq.heappop(values)
        print(val)

    # Part B
    print()
    print("Part B")
    customers = []
    heapStartTime = time.time()
    for i in range(1000):
        customer = Customer(random.randint(1, 5), i+1, names())
        heapq.heappush(customers, (customer.getPriority(), customer.getId(), customer))
    for i in range(10):
        c = heapq.heappop(customers)
        print(f"{'Customer: '}{c[2].getName():{'15'}}{'Priority: '}{c[2].getPriority():{'<5'}}ID: {c[2].getId():{'<5'}}")
    heapEndTime = time.time()
    print(f"Time for heap to process: {heapEndTime - heapStartTime}")
    print()

    # Part C
    print("As a list")
    customerList = []
    listStartStamp = time.time()
    for i in range(1000):
        customer = Customer(random.randint(1, 5), i+1, names())
        customerList.append(customer)
    priorityCustomers = []
    while len(priorityCustomers) <= 10:
        priorities = [customer.getPriority() for customer in customerList]
        lowestPriority = min(priorities)
        for customer in customerList:
            if customer.getPriority() == lowestPriority:
                priorityCustomers.append(customerList.pop(customerList.index(customer)))
    for i in range(10):
        customer = priorityCustomers.pop(0)
        print(f"{'Customer: '}{customer.getName():{'15'}}{'Priority: '}{customer.getPriority():{'<5'}}ID: {customer.getId():{'<5'}}")
    listEndStamp = time.time()
    print(f"Time for list to process: {listEndStamp - listStartStamp}")
    if (listEndStamp - listStartStamp) > (heapEndTime - heapStartTime):
        print("Heap sort was faster.")
    else:
        print("Sorting with loops was faster.")







if __name__ == '__main__':
    main()

