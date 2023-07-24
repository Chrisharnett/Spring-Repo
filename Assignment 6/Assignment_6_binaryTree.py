#!/usr/bin/env/python3

import random
import time

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


    def printTreeInOrder(self):
        if self.left:
            self.left.printTreeInOrder()
        print(self.data)
        if self.right:
            self.right.printTreeInOrder()

    def printTreePreOrder(self):
        print(self.data)
        if self.left:
            self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()

    def printTreePostOrder(self):
        if self.left:
            self.left.printTreePostOrder()
        if self.right:
            self.right.printTreePostOrder()
        print(self.data)

    def binaryTreeSearch(self, valToSearchFor):
        if valToSearchFor == self.data:
            return True
        elif valToSearchFor < self.data:
            if self.left is None:
                return False
            return self.left.binaryTreeSearch(valToSearchFor)
        elif valToSearchFor > self.data:
            if self.right is None:
                return False
            return self.right.binaryTreeSearch(valToSearchFor)

def searchFor(values, valToSearchFor):
    for val in values:
        if val == valToSearchFor:
            return True
    return False

def main():
    # Part and c
    values = [5, 6, 12, 2, 1, 4, 13]
    root = Node(5)
    for number in values[1:]:
        root.insert(number)
    print("In Order traversal")
    root.printTreeInOrder()
    print()
    print("Pre Order Traversal")
    root.printTreePreOrder()
    print()
    print("Post Order Traversal")
    root.printTreePostOrder()

    # Part d
    randomValues = []
    tree = Node(500000)
    treeCount = 0
    listCount = 0
    # create binary tree and list
    for i in range(100000):
        n = random.randint(1, 1000000)
        tree.insert(n)
        randomValues.append(n)
    # create a list of values to find
    valuesToFind  = []
    for i in range(100):
        valuesToFind.append(random.randint(1000, 2000))

    # test binary tree search
    treeStartStamp = time.time()
    for value in valuesToFind:
        isValInTree = tree.binaryTreeSearch(value)
        if isValInTree:
            treeCount += 1
    treeEndStamp = time.time()

    # test list search
    listStartStamp = time.time()
    for value in valuesToFind:
        isValInTree = searchFor(randomValues, value)
        if isValInTree:
            listCount += 1
    listEndStamp = time.time()
    print()
    print(f"Binary Tree: {treeCount} items were found. Search took {treeEndStamp - treeStartStamp} seconds.")
    print(f"List: {listCount} items were found. Search took {listEndStamp - listStartStamp} seconds.")


if __name__ == '__main__':
    main()
