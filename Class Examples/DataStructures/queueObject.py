class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self):
        name = input("Enter your name to join the queue: ")
        self.__list.append(name)

    def dequeue(self):
        if self.containsEntry():
            raise IndexError("There are no customers in the queue.")
        else:
            customer = self.__list.pop(0)
            print(f"{customer.title()} can pick up their XBox Series C Console.")

class Stack:
    def __init__(self):
        pass

    def push(self, value):
        pass

    def hasItems(self):
        pass

    def containsEntry(self):
        if 0 >= len(self.__list):
            return False
        else:
            return True
