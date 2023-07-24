from dataclasses import dataclass

@dataclass
class Temp:
    __fahrenheit: float = 32
    __celsius: float = 0

    def setCelsius(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = self.__celsius * 9/5 + 32

    def setFahrenheit(self, fahrenheit):
        self.__fahrenheit = fahrenheit
        self.__celsius = (fahrenheit - 32) * 5/9

    def getCelsius(self):
        return round(self.__celsius, 2)

    def getFahrenheit(self):
        return round(self.__fahrenheit, 2)

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    temp = Temp()
    for t in range(0, 212, 40):
        temp.setFahrenheit(t)
        print(temp.getFahrenheit(), "Fahrenheit equals", temp.getCelsius(), "Celsius")
    
    for t in range(0, 100, 20):
        temp.setCelsius(t)
        print(temp.getCelsius(), "Celsius equals", temp.getFahrenheit(), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

