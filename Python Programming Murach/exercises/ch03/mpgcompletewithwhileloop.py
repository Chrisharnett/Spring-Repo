#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

#Add a while loop
while True:
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:   "))
    #add input of gas cost
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost must be greater than zero. Please try again")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_cost = round(gallons_used * cost_per_gallon, 2)
        cost_per_mile = round(total_cost / miles_driven, 2)
        
        print("Miles Per Gallon:          ", mpg)
        print("Total Cost:     ", "$",total_cost)
        print("Cost per mile:    ", "$",cost_per_mile)
    if (keepGoing := input ("Would you like to do it again?  ").upper() != "Y"):
        break
    #calculate total gas cost
print()
print("Bye!")



