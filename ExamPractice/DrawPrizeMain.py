#! usr/bin/env/python3
from DrawPrize import *

def main():
    drawPrize = DrawPrize(1, 5, "saxophone")
    while True:
        ticket = drawPrize.giveTicket()
        if ticket == 'No More Tickets':
            break
        else:
            print("Ticket " + str(ticket) + ": " + drawPrize.checkTicket(ticket))


if __name__ == '__main__':
    main()