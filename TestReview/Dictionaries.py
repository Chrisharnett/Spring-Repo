#!/usr/bin/env/python3

def main():
    # Create a dictionary.
    dict = {"Title": "Soul Station",
            "Artist": "Hank Mobley",
            "Year": 1960}

    print(dict)
    # Accessing a value
    print(dict["Title"])

    # Setting a value
    dict["Title"] = "Combustication"
    dict["Artist"] = "Medeski, Martin and Wood"
    dict["Year"] = 1998
    print(dict)

    # Add a key/value pair
    dict["Genre"] = "Jazz Fusion"
    print(dict)

    # check if a KEY is in t a dictionary
    # album = "Everybody Digs Bill Evans"
    # album = "Soul Station"
    album = "Title"
    if album in dict:
        print("true")
    else:
        print("false")

    # return a value
    print(dict.get("Title"))

    # delete an item
    item = "Year"
    if item in dict:
        thisItem = dict[item]
        # del dict[item]
        dict.pop(item)

    print(dict)

    for detail in dict:
        print(f"{detail} : {dict[detail]}")


if __name__ == '__main__':
    main()