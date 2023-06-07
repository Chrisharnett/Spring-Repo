class Car:
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
