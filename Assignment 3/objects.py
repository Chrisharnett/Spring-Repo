from dataclasses import dataclass

@dataclass
class Rectangle:
    __height: int = 1
    __width: int = 1

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        rectangle = "*  " * self.__width + "\n"
        for i in range(self.__height - 2):
            rectangle += "*  " + ("   " * (self.__width - 2)) + "*\n"
        rectangle += "*  " * self.__width
        return rectangle

class Square(Rectangle):

    def __init__(self, length):
        Rectangle.__init__(self, length, length)








