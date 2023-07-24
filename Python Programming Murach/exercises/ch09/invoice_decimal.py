#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale


# display a title
print("The Invoice program")
print()

locale.setlocale(locale.LC_ALL, "en_US")

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    shipping_cost = subtotal * Decimal(0.085)
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax

    order_total = locale.currency(order_total, grouping=True)
    invoice_total = locale.currency(invoice_total, grouping=True)

    spec_numbers = "10,"
    spec_currency = ">10"
    column_width = "20"
    # display the results
    print(f"{'Order total':{column_width}}{order_total:{spec_currency}}")
    print(f"{'Discount amount':{column_width}}{discount:{spec_numbers}}")
    print(f"{'Subtotal':{column_width}}{subtotal:{spec_numbers}}")
    print(f"{'Shipping Cost':{column_width}}{shipping_cost:{spec_numbers}}")
    print(f"{'Sales tax':{column_width}}{sales_tax:{spec_numbers}}")
    print(f"{'Invoice total':{column_width}}{invoice_total:{spec_currency}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
