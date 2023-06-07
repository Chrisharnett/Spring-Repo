#!/usr/bin/env/python3

# from carWithoutDataclass import Car
from objects import *

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
    carDealerShip = CarDealership(inventory)
    print("We Sell Cars!!")
    print()
    while True:
        action = userMenu()
        print()
        if action == 'list':
            print(carDealerShip.listInventory())
        elif action == 'add':
            carDealerShip.addCar()
        elif action == 'delete':
            carDealerShip.deleteCar()
        elif action == 'search':
            carDealerShip.search()
        elif action == 'q':
            break
        else:
            print("Invalid selection. Try again.")
    print("Bye")


if __name__ == '__main__':
    main()
