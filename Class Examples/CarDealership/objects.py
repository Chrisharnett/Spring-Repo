from dataclasses import dataclass

class CarDealership:
    def __init__(self, inventory):
        self.__inventory = []
        self.__inventory.append(Car('Camry', 5000, 185, 2010, 5))
        self.__inventory.append(Car('Fit', 4500, 110, 2012, 5))
        self.__inventory.append(Car('Ranger', 30000, 210, 2021, 5))

    @property
    def inventory(self):
        return self.__inventory

    def addCar(self):
        name = input("Enter car name")
        price = float(input("Enter price"))
        horsepower = float(input("Enter Horsepower"))
        year = int(input("Enter year"))
        passengers = int(input("Passengers: "))
        newCar = Car(name, price, horsepower, year, passengers)
        self.__inventory.append(newCar)

    def deleteCar(self):
        print(self.listInventory())
        carToDelete = int(input("Select the car to delete")) - 1
        car = self.__inventory.pop(carToDelete)
        print(f"{car.name} is removed from inventory.")
        print()

    def listInventory(self):
        inventoryString = ""
        for i, car in enumerate(self.__inventory, 1):
            car = f"{i}. {car.printCar()}\n"
            inventoryString += car
        return inventoryString

    def search(self):
        price = int(input("What's your round budget?"))
        for car in self.__inventory:
            if car.price <= price:
                car.printCar()

@dataclass
class Car:
    __name: str = ""
    __price: float = 0
    __horsepower: float = 0
    __year: int = 2000
    __passengers: int = 5

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def printCar(self):
        return f"{'Vehicle'} {self.name:{'10'}} {'Price:'} ${self.price:{'7'}} {'Horsepower:'} " \
               f"{self.__horsepower:{'5'}} {'Year:'} {self.__year:{'6'}} {'Passengers:'} {self.__passengers:{'3'}}"

class CarWithoutDataclass:
    def __init__(self, name, price, horsepower, year, passengers):
        self.__name = name
        self.__price = price
        self.__horsepower = horsepower
        self.__year = year
        self.__passengers = passengers

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def horsepower(self):
        return self.__horsepower

    @property
    def year(self):
        return self.__year

    @property
    def passengers(self):
        return self.__passengers

    def printCar(self):
        return f"{'Vehicle'} {self.name}; {'Price:'} ${self.price}; {'Horsepower:'} " \
               f"{self.__horsepower}; {'Year:'} {self.__year}; {'Passengers:'} {self.__passengers}"
