from objects import Queue
def getInLine(customers):
    name = input("Enter your name")
    customers.enqueue(name)


def processCustomer(customers):
    if customers.hasItems() == False:
        print("no customers in line")
    else:
        nextCustomer = customers.dequeue()
        print(f"{nextCustomer} has been given an xbox")
def printMenu():
    print("1. Get in line")
    print("2. Process customer")
    print("3. Exit")

def main():
    customers = Queue()
    while True:
        printMenu()
        choice = input("Enter your choice")
        if choice == "1":
            getInLine(customers)
        elif choice == "2":
            processCustomer(customers)
        elif choice == "3":
            break
        else:
            print("Invalid Option, Try again")




if __name__ == '__main__':
    main()
