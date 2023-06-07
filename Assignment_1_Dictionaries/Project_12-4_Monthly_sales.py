#!/usr/bin/env/python3

from decimal import Decimal
import sys
import locale as locale

locale.setlocale(locale.LC_ALL, "en_US")

FILENAME = 'monthly_sales.txt'

def readFile():
    sales = {}
    try:
        with open(FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                monthlySales = line.split("\t")
                sales.update({monthlySales[0]: Decimal(monthlySales[1])})
        return sales
    except FileNotFoundError as e:
        print("File not found.\n Exiting program. Bye!")
        sys.exit(1)
    except Exception as e:
        print("Unknown Exception, Closing Program")
        print(type(e), e)
        sys.exit(1)


def writeFile(sales):
    try:
        with open(FILENAME, "w") as file:
            for month in sales:
                file.write(f"{month}\t{sales[month]}\n")
    except Exception as e:
        print("Unknown Exception, closing Program")
        print(type(e), e)
        sys.exit(1)

def getMonth():
    return input("Enter 3 letter month: ").title()

def view(sales):
    month = getMonth()
    if month in sales:
        monthlySales = locale.format_string("%.2f", sales[month], grouping=True)
        print(f"Sales amount for {month} is {monthlySales}.")
    else:
        print("Invalid three-letter month.")


def edit(sales):
    month = getMonth()
    if month in sales:
        while True:
            try:
                salesAmount = Decimal(input("Sales Amount: "))
                sales[month] = salesAmount
                printSales = locale.format_string("%.2f", sales[month], grouping=True)
                print(f"Sales amount for {month} is {printSales}")
                writeFile(sales)
                return
            except ValueError:
                print("Invalid sales amount. Please enter a valid amount.")
    else:
        print("Invalid three letter month.")


def totals(sales):
    yearlyTotal = 0
    for month in sales:
        yearlyTotal += sales[month]
    monthlyAverage = yearlyTotal/12
    yearlyTotal = locale.format_string("%.2f", yearlyTotal, grouping=True)
    monthlyAverage = locale.format_string("%.2f", monthlyAverage, grouping=True)
    print(f"{'Yearly total:':{'20'}}{yearlyTotal}")
    print(f"{'Monthly average:':{'20'}}{monthlyAverage}")

def userMenu():
    print()
    print('COMMAND MENU')
    print(f"{'view':{'7'}} - View sales for specified month")
    print(f"{'edit':{'7'}} - Edit sales for specified month")
    print(f"{'totals':{'7'}} - View sales summary for year")
    print(f"{'exit':{'7'}} - Exit program")
    print()
    command = input("Command: ").lower()
    return command

def main():
    sales = readFile()
    print("Monthly Sales program")
    while True:
        command = userMenu()
        if command == "view":
            view(sales)
        elif command == "edit":
            edit(sales)
        elif command == "totals":
            totals(sales)
        elif command == "exit":
            break
        else:
            print("Command not recognized, please try again.")
    print("Bye!")


if __name__ == '__main__':
    main()
