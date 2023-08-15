#!/usr/bin/env/python3

def addCustomer(customers):
    name = input("Enter your name to get in line ")
    customers.append(name)
    return customers

def processCustomer(customers):
    if len(customers) > 0:
        customer = customers.pop(0)
        print(f"{customer.title()} can pick up their XBox Series C Console.")
        return customers
    else:
        print("There are no customers in line.")

def main():
    customers = []
    print("Welcome to the store")
    print()
    while True:
        print("1 - Get in line")
        print("2 - Process customer")
        choice = int(input("What would you like to do? "))
        if 1 == choice:
            customers = addCustomer(customers)
        elif 2 == choice:
            processCustomer(customers)
        choice = input("Continue (y/n): ")
        if "y" != choice.lower():
            break

if __name__ == '__main__':
    main()
