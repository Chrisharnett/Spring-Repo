#!/usr/bin/env/python3

def search(inventory):
    minPrice = int(input("Enter the minimum price"))
    maxPrice = int(input("Enter the maximum price"))
    i = 1
    for bike in inventory:
        if minPrice < int(bike["Price"]) < maxPrice:
            print(f"{i} {bike['name']} {bike['Price']} {bike['size']} {bike['colour']}")
            i += 1

def remove(inventory):
    listInventory(inventory)
    toRemove = int(input("Enter the number for the bike to delete."))
    if len(inventory) >= toRemove > 0:
        bike = inventory.pop(toRemove - 1)
        print(f"Removed {bike['name']}.")
    return inventory

def add(inventory):
    name = input("Enter bicycle name")
    price = input("Enter bicycle price")
    size = input("Enter bicycle size")
    color = input("Enter bicycle color")
    inventory.append({"name": name, "Price": price, "size": size, "colour": color})
    return inventory

def listInventory(inventory):
    i = 1
    for bike in inventory:
        print(f"{i} {bike['name']} {bike['Price']} {bike['size']} {bike['colour']}")
        i += 1

def userMenu():
    print("Command Menu")
    print("list - List all bicycles")
    print("add - add a bicycle ")
    print("del - delete a bicycle")
    print("search - Search for a bicycle based on a min and max price")
    print("exit - Exit program")
    print()

def main():
    print("Welcome to Eric's Bicycle Shop")
    inventory = [{"name": "Specialized Stumpjumper", "Price": 2999.99, "size": "Large", "colour": "red"},
                 {"name": "KHS Alite Team", "Price": 2350.99, "size": "Medium", "colour": "Blue"},
                 {"name": "Norco Sasquatch", "Price": 1239.99, "size": "Medium", "colour": "Green"}]
    userMenu()
    while True:
        option = input("Command: ").lower()
        if "list" == option:
            listInventory(inventory)
        elif "add" == option:
            inventory = add(inventory)
        elif "del" == option:
            inventory = remove(inventory)
        elif "search" == option:
            search(inventory)
        elif "exit" == option:
            break
        else:
            print("Invalid selection, try again.")
    print()
    print("Bye!")


if __name__ == '__main__':
    main()
