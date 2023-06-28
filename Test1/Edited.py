#!/usr/bin/env/python3

from DrawPrize import *
from random import Random
def main():
    drawPrize = DrawPrize(1, 5, "bicycle")
    # winner = random.randint(1, 5)
    ticketsOut = []
    while True:
        ticket = drawPrize.giveTicket(ticketsOut)
        prize = drawPrize.checkTicket(ticket)
        if "No more tickets" == prize:
            break
        else:
            print(f"Checking ticket number {ticket}")
            print(prize)
            ticketsOut.append(ticket)

if __name__ == '__main__':
    main()