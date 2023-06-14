from dataclasses import dataclass

@dataclass
class Person:
    __firstName: str = ""
    __lastName: str = ""
    __email: str = ""

    @property
    def name(self):
        return f"{self.__firstName.title()} {self.__lastName.title()}"

    @property
    def email(self):
        return self.__email
@dataclass
class Customer(Person):
    __customerNumber: str = ""

    @property
    def customerNumber(self):
        return self.__customerNumber

@dataclass
class Employee(Person):
    __ssn: str = ""

    @property
    def ssn(self):
        return self.__ssn
