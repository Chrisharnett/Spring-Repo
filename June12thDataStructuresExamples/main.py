#

def main():

   ericCards = {"Wayne Gretzky":2, "Mario Lemieux": 3, "Sidney Crosby": 1, "Austin Mathews" : 1, "Jaromir Jagr" : 2 }

   additionalCards = {"Wayne Gretzky":1, "Alexander Ovechkin": 3, "Mark Messier" : 2, "Bobby Hull": 1 }

   cardSet = set()

   for player in ericCards:
       cardSet.add(player)

   for player in additionalCards:
       cardSet.add(player)

   print("All of the cards are")
   for card in cardSet:
       print(card)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
