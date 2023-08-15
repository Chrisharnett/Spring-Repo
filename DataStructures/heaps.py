import heapq
import random

class Person:
    def __init__(self, id):
        self.id = id
    def __lt__(self, nxt):
        return self.id < nxt.id
    def __str__(self):
        return f"person with id {self.id}"



def main():
    eric = Person(45)
    dave = Person(33)

    people = [eric, dave]

    heapq.heapify(people)
    for val in people:
        print(val)
    # use heap to sort 10 random numbers
    '''heap = []
    for i in range(10):
        heapq.heappush(heap, random.randint(10, 50))
    while len(heap) > 0:
        value = heapq.heappop(heap)
        print(value)


    H = [21, 1, 45, 78, 5]
    heapq.heapify(H)
    print(H)

    heapq.heappush(H, 8)
    print(H)

    heapq.heappop(H)
    print(H)'''

if __name__ == '__main__':
    main()