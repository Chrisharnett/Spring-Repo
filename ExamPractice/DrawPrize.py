#!/user/bin/env/python3

import random

class DrawPrize:
    def __init__(self, lowNumber, highNumber, prize):
        self.__lowNumber = lowNumber
        self.__highNumber = highNumber
        self.__prize = prize
        self.__tickets = list(range(lowNumber, highNumber + 1))
        self.__ticketsOut = []
        self.__winningNumber = random.randint(lowNumber, highNumber)

    def giveTicket(self):
        while True:
            if 0 == len(self.__tickets):
                return "No More Tickets"
            else:
                return self.__tickets.pop(random.randint(0, len(self.__tickets)-1))
                # if ticket in self.__ticketsOut:
                #     continue
                # else:
                #     self.__ticketsOut.append(ticket)
                #     return ticket

    def checkTicket(self, n):
        if n == self.__winningNumber:
            return "You win a " + self.__prize
        else:
            return "Sorry, no prize."



