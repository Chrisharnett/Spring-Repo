from dataclasses import dataclass

@dataclass
class Rectangle:
    __height: int = 1
    __width: int = 1

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)

    def area(self):
        return self.__width * self.__height

    def consoleArt(self):
        print("* " * self.__width)
        for i in range(self.__height - 2):
            print("* " + ("  " * (self.__width - 2)) + "*" )
        print("* " * self.__width)


