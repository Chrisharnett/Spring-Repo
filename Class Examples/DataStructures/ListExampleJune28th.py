
import time
import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
       # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return False
            return self.left.search(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return False
            return self.right.search(lkpval)
        else:
            return True

def searchFor(values, valToSearchFor):
    count = 0
    for val in values:
        count += 1
        if val == valToSearchFor:
            return True
    print(f"number of operations is {count}")
    return False

def main():
    values = []
    root = Node(2500000)
    for i in range(1000000):
        if i % 100000 == 0:
            print(i)
        root.insert(random.randint(1, 5000000))
        values.append(random.randint(1, 5000000))
    root.insert(123456);
    print("starting search using binary search tree")
    startStamp = time.time();
    found = root.search(10) #searchFor(values, 10);
    endStamp = time.time();
    print(endStamp - startStamp)
    print(f"Was found is {found}")

    print("starting search using list")
    startStamp = time.time();
    found = searchFor(values, 10);
    endStamp = time.time();
    print(endStamp - startStamp)
    print(f"Was found is {found}")

if __name__ == "__main__":
    main()