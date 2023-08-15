from objects import Queue

def stutter(queue):
    duplicatedQueue = Queue()

    while( queue.hasItems()):
        value = queue.dequeue()
        duplicatedQueue.enqueue(value)
        duplicatedQueue.enqueue(value)

    return duplicatedQueue


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue = stutter(queue)

    while( queue.hasItems()):
        print(queue.dequeue())

if __name__ == "__main__":
    main()
