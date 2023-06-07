
class Customer:
    def __init__(self, customerId, firstName, lastName, company, address, city, state, zip):
        self.__customerId = customerId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__company = company
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip

    @property
    def customerId(self):
        return self.__customerId

    @property
    def nameAndAddress(self):
        nameAndAddress = ""
        nameAndAddress = f"{self.__firstName} {self.__lastName}\n"
        if self.__company != "":
            nameAndAddress += f"{self.__company}\n"
        nameAndAddress += f"{self.__address}\n{self.__city}, {self.__state}, {self.__zip}"

        return nameAndAddress
