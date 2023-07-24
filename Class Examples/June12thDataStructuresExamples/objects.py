class Queue:

    def __init__(self):
        self.__list = []

    def dequeue(self):
        if self.hasItems() == False:
            raise IndexError("Can't perform dequeue, There are no items in the queue")
        return self.__list.pop(0)

    def enqueue(self, value):
        self.__list.append(value)

    def hasItems(self):
        return len(self.__list) > 0

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value);

    def pop(self):
        return self.__list.pop();

    def hasItems(self):
        return len(self.__list) > 0


class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
        self.endval = None

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

        self.endval.nextval = nextNode
        self.endval = nextNode


    def printList(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval