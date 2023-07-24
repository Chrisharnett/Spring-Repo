from dice import Dice, Die


def main():
    print("The Dice Roller program")
    for i in range(1, 7):
        die = Die()
        die.value = i
        print()
        print(die.image)


    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    choice = "y"
    while choice.lower() == "y":
        # roll the dice
        dice.rollAll()

        # display to user
        print("YOUR ROLL: ", end="")
        for die in dice.list:
            print()
            print(die.image, end=" ")
        print()
        print()
        print(f"Total is {dice.getTotal()}")

        print("\n")

        choice = input("Roll again? (y/n): ")

    print("Bye!")


if __name__ == "__main__":
    main()
