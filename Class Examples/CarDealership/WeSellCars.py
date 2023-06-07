#!/usr/bin/env/python3

# from carWithoutDataclass import Car
from objects import *
def addCar(inventory):
    name = input("Enter car name")
    price = float(input("Enter price"))
    horsepower = float(input("Enter Horsepower"))
    year = int(input("Enter year"))
    passengers = int(input("Passengers: "))
    newCar = Car(name, price, horsepower, year, passengers)
    inventory.append(newCar)


def deleteCar(inventory):
    listInventory(inventory)
    carToDelete = int(input("Select the car to delete")) - 1
    inventory.pop(carToDelete)


def search(inventory):
    price = int(input("What's your round budget?"))
    for car in inventory:
        if car.price <= price:
            car.printCar()
    else:
        print("No cars in price range.")

def listInventory(inventory):
    for i, car in enumerate(inventory, 1):
        print(f"{i}. {car.printCar()}")
    print()

def userMenu():
    print("List = List all cars\n"
          "Add = Add car\n"
          "Delete = Delete car\n"
          "Search = Search for a car.\n"
          "Q = Quit")
    return input("Make a selection:").lower()

def main():
    camry = Car('Camry', 5000, 185, 2010, 5)
    fit = Car('Fit', 4500, 110, 2012, 5)
    ranger = Car('Ranger', 30000, 210, 2021, 5)
    inventory = [camry, fit, ranger]
    print("We Sell Cars!!")
    print()
    while True:
        action = userMenu()
        print()
        if action == 'list':
            listInventory(inventory)
        elif action == 'add':
            addCar(inventory)
        elif action == 'delete':
            deleteCar(inventory)
        elif action == 'search':
            search(inventory)
        elif action == 'q':
            break
        else:
            print("Invalid selection. Try again.")
    print("Bye")


if __name__ == '__main__':
    main()
