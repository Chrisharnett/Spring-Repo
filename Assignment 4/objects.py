
class Queue:
    def __init__(self):
        self.__list = []

    def __iter__(self):
        for item in self.__list:
            yield item

    def enqueue(self, value):
        self.__list.append(value)

    def dequeue(self):
        if 0 < self.length():
            return self.__list.pop(0)

    def peek(self):
        return self.__list[0]

    def length(self):
        return len(self.__list)

    def __str__(self):
        string = ""
        for item in self.__list:
            string += f"{item}, "
        string = string.removesuffix(", ")
        return string

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        return self.__list[-1]

    def clear(self):
        self.__list.clear()

    def length(self):
        return len(self.__list)

    def is_empty(self):
        return 0 == len(self.__list)

    def __str__(self):
        string = ""
        for item in self.__list:
            string += f"{item}, "
        return string.removesuffix(", ")


