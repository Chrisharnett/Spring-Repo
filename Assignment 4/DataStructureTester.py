#!/usr/bin/env/python3

from objects import *
import random

def numberString(numberList):
    numberString = ""
    for number in numberList:
        numberString += f"{number}, "
    return numberString.removesuffix(", ")

def queueTest(numberList):
    print()
    print("Queue Test")
    print(f"Push a list of numbers to a queue.")
    print(f"List: {numberString(numberList)}")
    queue = Queue()
    for number in numberList:
        queue.enqueue(number)
    print(f"Queue: {queue}")
    print(f"Queue Length: {queue.length()}")
    print(f"Peek at the front element in the queue: {queue.peek()}")
    print(f"Check that we only peeked at the front element and that it's still in the queue.")
    print(queue)
    print("Dequeue each element from queue.")
    while 0 < queue.length():
        print(queue.dequeue())

def stackTest(numberList):
    print()
    print("Stack Test")
    print(f"Push a list of numbers to a stack")
    print(f"List: {numberString(numberList)}")
    stack = Stack()
    for number in numberList:
        stack.push(number)
    print(f"Stack: {stack}")
    print(f"Stack Length: {stack.length()}")
    print(f"Peek at the top element in the stack: {stack.peek()}")
    print(f"Check that we only looked at the top element, and it's still in the stack.")
    print(stack)
    print("Pop each element off of the stack.")
    while 0 < stack.length():
        print(stack.pop())
    if stack.is_empty():
        print("Stack is empty.")
    print("Create a new stack of numbers.")
    for i in range(random.randint(1, 10)):
        stack.push(random.randint(1, 1000))
    print(stack)
    print("Clear the stack.")
    stack.clear()
    if stack.is_empty():
        print("Stack is cleared.")



def main():
    numberList = []
    for i in range(random.randint(1, 10)):
        numberList.append(random.randint(1, 1000))
    stackTest(numberList)
    print()
    queueTest(numberList)

if __name__ == '__main__':
    main()