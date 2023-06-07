#!/usr/bin/env/python3


def analyzeCode(code, postalCodes):
    cityOrTown = "urban"
    if code[1] == '0':
        cityOrTown = "rural"
    if code[0].upper() in postalCodes:
        print(f"This code is for an {cityOrTown} address in {postalCodes[code[0].upper()]}")
    else:
        print("This is not a valid Canadian postal code.")


def getCode():
    while True:
        code = input('Enter a valid Canadian Postal Code: ')
        code = code.replace(" ", "")
        if len(code) == 6 or code.lower() == "exit":
            return code
        else:
            print("This is not a valid Canadian Postal Code, please try again.")

def main():
    postalCodes = {"A": "Newfoundland and Labrador",
                   "B": "Nova Scotia",
                   'C': 'Prince Edward Island',
                   'E': 'New Brunswick',
                   'G': 'Quebec',
                   'H': 'Quebec',
                   'J': 'Quebec',
                   'K': 'Ontario',
                   'L': 'Ontario',
                   'M': 'Ontario',
                   'N': 'Ontario',
                   'P': 'Ontario',
                   'R': 'Manitoba',
                   'S': 'Saskatchewan',
                   'T': 'Alberta',
                   'V': 'British Columbia',
                   'X': 'Nunavut or Northwest Territories',
                   'Y': 'Yukon'}
    print("Postal Code Checker")
    while True:
        print()
        print("type exit to exit")
        code = getCode()
        if code.lower() == "exit":
            break
        else:
            analyzeCode(code, postalCodes)
    print("Bye!")


if __name__ == '__main__':
    main()
