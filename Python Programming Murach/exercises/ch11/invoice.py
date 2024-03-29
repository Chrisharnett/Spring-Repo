#!/usr/bin/env python3

from datetime import datetime, timedelta
from datetime import date


def get_invoice_date():
    invoice_date = date.today() + timedelta(days=1)
    while True:
        try:
            invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
            invoice_date_time = datetime.strptime(invoice_date_str, "%m/%d/%Y")
            invoice_date = datetime.date(invoice_date_time)
            if invoice_date <= date.today():
                return invoice_date
            else:
                print("Date must be today or earlier. Try Again")
        except ValueError:
            print("Invalid date format. Try again")
            print()



def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
