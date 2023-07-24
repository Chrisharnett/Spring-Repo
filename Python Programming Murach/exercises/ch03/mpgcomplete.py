#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

#Add a while loop
while (keepGoing := input("Would you like to perform calculation? (Y/n)").upper()) == "Y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    #add input of gas cost
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)
    #calculate total gas cost
print()
print("Bye!")



