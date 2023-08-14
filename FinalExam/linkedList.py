#!/usr/bin/env/python3

class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None


class LinkedList:
    def __init__(self):
        self.headVal = None
        self.endVal = None

    def insert(self, val):
        nextNode = Node(val)
        nextNode.nextVal = self.headVal
        if self.headVal is None:
            self.endVal = nextNode
        self.headVal = nextNode

    def insert_end(self, val):
        nextNode = Node(val)
        if self.headVal is None:
            self.headVal = nextNode
            self.endVal = nextNode
            return
        self.endVal.nextVal = nextNode
        self.endVal = nextNode

    def insert_after(self, addAfterVal, valToAdd):
        newNode = Node(valToAdd)
        if valToAdd == self.endVal:
            self.endVal.nextVal = newNode
            self.endVal = newNode
        checkVal = self.headVal
        while checkVal is not None:
            if checkVal.dataVal == addAfterVal:
                newNode.nextVal = checkVal.nextVal
                checkVal.nextVal = newNode
                return
            else:
                checkVal = checkVal.nextVal

    def find(self, val):
        checkVal = self.headVal
        newNode = Node(val)
        while checkVal is not None:
            if checkVal.dataVal == newNode:
                return True
            else:
                checkVal = checkVal.nextVal
        return False

    def remove(self, val):
        checkVal = self.headVal
        if checkVal.dataVal == val:
            if checkVal.nextVal is None:
                self.headVal = None
            else:
                checkVal = checkVal.nextVal
                checkVal.nextVal = checkVal.nextVal.nextVal
            return
        while checkVal is not None:
            if checkVal.nextVal.dataVal == val:
                if checkVal.nextVal == self.endVal:
                    checkVal.nextVal = None
                    self.endVal = checkVal
                    return
                else:
                    checkVal.nextVal = checkVal.nextVal.nextVal
                    return
            else:
                checkVal = checkVal.nextVal
        return

    def is_empty(self):
        if self.headVal is None:
            return True
        return False

    def get_count(self):
        counter = 0
        val = self.headVal
        while val is not None:
            counter += 1
            val = val.nextVal
        return counter

    def printList(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

# Testing for above methods
def main():
    carList1 = LinkedList()
    carList1.insert("Camry")
    carList1.insert("F150")
    carList1.insert("Mustang")

    carList2 = LinkedList()
    carList2.insert_end("Camry")
    carList2.insert_end("F150")
    carList2.insert_end("Mustang")

    carList1.insert("First car")
    carList1.insert_end("last car")

    carList1.printList()
    print()
    carList2.printList()
    print()
    print("Insert Outback after F150 in list1")
    carList1.insert_after("F150", "Outback")
    carList1.printList()
    print("insert Matrix to the end of the list")
    carList1.insert_after("Camry", "Matrix")
    carList1.printList()
    print()
    print(carList1.find("Ascent"))
    print()
    print("Remove Outback from list 1")
    carList1.remove("Outback")
    carList1.printList()
    print()
    print("Check for empty")
    print(carList2.is_empty())
    print("Remove all items. Should output true")
    carList2.remove("F150")
    carList2.remove("Mustang")
    carList2.remove("Camry")
    print(carList2.is_empty())

    print(carList1.get_count())
    print(carList2.get_count())

if __name__ == '__main__':
    main()