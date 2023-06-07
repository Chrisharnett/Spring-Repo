#!/usr/bin/env/python3

def main():
    # strings as keys and values
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico",
                 "GB": "Great Britain"}

    #Adding to a dictionary
    countries["DE"] = "Germany"
    countryKey = "CA"

    # Deleting an item
    del countries["CA"]
    print(countries)

    # using pop command. Will return the value that's deleted
    country = countries.pop(countryKey, "Default message to display when the key doesn't exist")
    print(country)

    print("Access via key")
    # Check if a key exists and access with the key
    if countryKey in countries:
        print(countries[countryKey])
    else:
        print("Key not found")

    # Access a dictionary using get method.
    print("Using the GET Method")
    country = countries.get(countryKey, "Custom message that item isn't there.")
    print(country)
    # To loop through the keys - .keys() here is optional
    for code in countries.keys():
        print(f"Key {code} with value of {countries[code]}")

    for item in countries.items():
        print(f"Key: {item[0]} Value: {item[1]}")

    # Use clear method to clear all the data.
    countries.clear()


if __name__ == '__main__':
    main()

