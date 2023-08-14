import random
from random import Random

class DrawPrize:
    def __init__(self, lowNumber, highNumber, prize):
        self.__highNumber = highNumber
        self.__lowNumber = lowNumber
        self.__prize = prize
        self.__winningNumber = random.randint(lowNumber, highNumber)

    def giveTicket(self, ticketsOut):
        if len(ticketsOut) == self.__highNumber:
            return "No more tickets"
        while True:
            ticket = random.randint(self.__lowNumber, self.__highNumber)
            if ticket not in ticketsOut:
                return ticket

    def checkTicket(self, ticket):
        if ticket != self.__winningNumber:
            return "Try again"
        else:
            return f"You win {self.__prize}"

        