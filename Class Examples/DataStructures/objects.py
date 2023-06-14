
class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, value):
        self.__list.append(value)

    def dequeue(self):
        if self.hasItems():
            return self.__list.pop(0)

    def hasItems(self):
        if 0 >= len(self.__list):
            return False
        else:
            return True

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        return self.__list.pop()

    def hasItems(self):
        if 0 >= len(self.__list):
            return False
        else:
            return True

class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def addNode(self, value):
        nextNode = Node(value)
        nextNode.nextval = self.headval
        if self.headval == None:
            self.endval = nextNode
        self.headval = nextNode


    def addNodeToBack(self, value):
        nextNode = Node(value)
        if self.headval == None:
            self.headval = nextNode
            self.endval = nextNode
            return

        self.endval.nextNode = nextVal
        self.endval = nextNode

        # currentval = self.headval
        # while currentval.nextval is not None:
        #     currentval = currentval.nextval
        # currentval.nextval = nextNode