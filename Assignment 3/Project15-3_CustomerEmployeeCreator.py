#!/usr/bin/env/python3

from person import *
def dataEntry(choice):
    print("DATA ENTRY")
    firstName = input("First name: ")
    lastName = input("Last name: ")
    email = input("Email: ")
    if "c" == choice:
        customerNumber = input("Number: ")
        return Customer(firstName, lastName, email, customerNumber)
    elif "e" == choice:
        ssn = input("SSN: ")
        return Employee(firstName, lastName, email, ssn)

def printPerson(person):
    col = '12'
    nameEmail = f"{'Name:':{col}}{person.name}\n{'Email:':{col}}{person.email}"
    if isinstance(person, Customer):
        print("CUSTOMER")
        print(nameEmail)
        print(f"{'Number:':{col}}{person.customerNumber}")
    elif isinstance(person, Employee):
        print("EMPLOYEE")
        print(nameEmail)
        print(f"{'Number:':{col}}{person.ssn}")


def main():
    print("Customer/Employee Data Entry")
    print()
    while True:
        choice = input("Customer or employee? (c/e): ")
        print()
        person = dataEntry(choice)
        print()
        printPerson(person)
        print()
        choice = input("Continue? (y/n)")
        print()
        if "y" != choice:
            break

    print("Bye!")






if __name__ == '__main__':
    main()

