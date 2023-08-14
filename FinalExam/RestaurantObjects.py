#! user/bin/env/python3

class Restaurant:
    def __init__(self):
        self.__menuItems = []
        self.__bookTable = []
        self.__customerOrders = []

    def addItemToMenu(self, dishName, price):
        self.__menuItems.append([dishName, price])

    def bookTables(self, tableNumber):
        if tableNumber in self.__bookTable:
            return "Table is already reserved"
        else:
            self.__bookTable.append(tableNumber)

    def customerOrder(self, tableNumber, order):
        self.__customerOrders.append([tableNumber, order])

    def __str__(self):
        col = 20
        menu = ''
        for item in self.__menuItems:
            menu += f"{item[0]:{col}}${item[1]}\n"
        return menu

    def printTableReservations(self):
        resos = ''
        for table in self.__bookTable:
            resos += f"Table {table}\n"
        print(resos)

    def printCustomerOrders(self):
        orders = ''
        for order in self.__customerOrders:
            orders += f"Table {order[0]}: {order[1]}\n"
        print(orders)


def main():
    resto = Restaurant()

    # Add Items to meny
    resto.addItemToMenu("Pizza", 13.99)
    resto.addItemToMenu("Burrito", 9.99)
    resto.addItemToMenu("Butter tofu", 14.99)
    resto.addItemToMenu("Spicy Salmon Roll", 12.99)
    resto.addItemToMenu("Chick Pea Burger", 16.99)
    resto.addItemToMenu("Chocolate Cake", 4.99)

    # Book Tables
    resto.bookTables(1)
    resto.bookTables(2)
    resto.bookTables(3)

    # Order Items
    resto.customerOrder(1, "Spicy Salmon Roll")
    resto.customerOrder(1, "Burrito")
    resto.customerOrder(2, "Chick Pea Burger")
    resto.customerOrder(3, "Chocolate Cake")

    print("\nWelcome to Symonds Cafe")
    print("Menu")
    print(resto)
    print("Current reservations:")
    resto.printTableReservations()
    print("Current orders:")
    resto.printCustomerOrders()


if __name__ == '__main__':
    main()


