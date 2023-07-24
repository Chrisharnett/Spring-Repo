#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter end to end input")
print("======================")

    
# initialize variables
counter = 0
score_total = 0
test_score = 0
while True:
    while test_score := input("Enter the test score") != "end":
        test_score = int(test_score)
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print(f"Test score must be from 0 through 100. "
                  f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")

    keepGoing = input("Would you like to go again? (Y/N)?")
    if keepGoing !="Y":
        break
print()
print("Bye!")


