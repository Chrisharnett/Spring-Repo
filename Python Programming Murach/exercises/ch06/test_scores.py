#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    counter = 0
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    score_total = 0
    for score in scores:
        score_total += score
    average = score_total/len(scores)
    low_score = min(scores)
    high_score = max(scores)
    
    sorted_scores = sorted(scores)
    if len(scores)%2 == 0:
        position1=int((len(sorted_scores)/2))        
        position2=int((len(sorted_scores)/2)-1)
        score1=sorted_scores[position1]
        score2=sorted_scores[position2]
        median_score = (score1+score2)/2
    elif len(scores)%2 == 1:
        position1 = int(len(sorted_scores)/2)
        median_score = sorted_scores[position1]

                
    # format and display the result
    print()
    print("Total:           ", score_total)
    print("Number of Scores:", len(scores))
    print("Average Score:   ", average)
    print("Low Score:       ", low_score)
    print("High Score:      ", high_score)
    print("Median Score:    ", median_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


