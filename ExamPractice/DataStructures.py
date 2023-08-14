class Queue:
    def __init__(self):
        self.__list = []
        
    def dequeue(self):
        if not self.hasItems():
            raise IndexError("No items in queue, cannot dequeue.")
        return self.__list.pop(0)
    
    def enqueue(self, val):
        self.__list.append(val)
        
    def hasItems(self):
        return len(self.__list) >0
    
class Stack: 
    def __init__(self):
        self.__list = []
        
    def push(self, val):
        self.__list.append(val)
        
    def pop(self):
        return self.__list.pop()
    
    def hasItems(self):
        return len(self.__list) >0
    
#Linked List

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class LinkedList:
    def __init__(self):
        self.headval = None
        self.endval = None
    
    def addNode(self, val):
        nextNode = Node(val)
        nextNode.nextval = self.headval
        if self.headval is None:
            self.endval = nextNode
        self.headval = nextNode
    
    def addNodeToBack(self, val):
        nextNode = Node(val)
        
        if self.headval is None:
            self.headval = nextNode
            self.endval = nextNode
            return
        self.endval.nextval = nextNode
        self.endval - nextNode
    
    def printList(self):
        printVal = self.headval
        while printVal is not None:
            print(printVal.dataval)
            printVal = printVal.nextval

# binary tree
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTreeInOrder(self):
        if self.left:
            self.left.printTreeInOrder()
        print(self.data)
        if self.right:
            self.printTreeInOrder()

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

    def binarySearchTree(self, valToFind):
        if valToFind == self.data:
            return True
        elif valToFind < self.data:
            if self.left is None:
                return False
            return self.left.binaryTreeSearch(valToFind)
        elif valToFind > self.data:
            if self.right is None:
                return False
            return self.right.binaryTreeSearch(valToFind)
        