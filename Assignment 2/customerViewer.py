#!/usr/bin/env/python3
import csv
from customer import Customer
import sys

FILENAME = "customers.csv"

def readFile():
    customerList = []
    try:
        with open(FILENAME, newline="\n") as file:
            next(file)
            reader = csv.reader(file)
            for row in reader:
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                customerList.append(customer)
        return customerList
    except FileNotFoundError:
        print("File not Found. Ending program.")
        sys.exit(1)
    except IndexError:
        print("Invalid .csv format. Ending program.")
        sys.exit(1)
    except Exception as e:
        print("Unexpected error occurred, exiting program.")
        sys.exit(1)


def main():
    print("Customer Viewer")
    customerList = readFile()
    while True:
        try:
            print()
            customerId = input("Enter customer ID: ")
            print()
            customerString = ""
            index = -1
            for customer in customerList:
                if customer.customerId == customerId:
                    index = customerList.index(customer)
            if index == -1:
                print("No customer with that ID.")
            else:
                print(customerList[index].nameAndAddress)
            print()
            another = input("Continue? (y/n): ")
            if another.lower() != 'y':
                break
        except ValueError:
            print("Invalid customer ID, please try again.")
    print()
    print('Bye')


if __name__ == '__main__':
    main()
