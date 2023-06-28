#!/usr/bin/env/python2
from objects import *
def mirror(queue):
    stack = Stack()
    string = ""
    for item in queue:
        stack.push(item)
    while 0 < stack.length():
        item = stack.pop()
        queue.enqueue(item)

def main():
    queue = Queue()
    stringList = ["coffee", "synth", "card", "pen"]
    for string in stringList:
        queue.enqueue(string)
    print(f"Original queue: {queue}")
    mirror(queue)
    print(f"Mirrored queue: {queue}")


if __name__ == '__main__':
    main()
