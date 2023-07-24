#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter the cost per gallon:\t"))

# calculate miles per gallon
mpg = round((miles_driven / gallons_used), 2)
total_gas_cost = round((gallons_used*cost_per_gallon), 2)
cost_per_mile = round((total_gas_cost/miles_driven), 2)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print()
print(f"(Total Gas Cost:\t\t{total_gas_cost}")
print()
print(f"(Cost per mile:\t\t\t{cost_per_mile}")
print("Bye!")


