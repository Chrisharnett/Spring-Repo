#!/usr/bin/env/python3

from objects import Stack

def main():
    stack = Stack()
    char = input("Enter a character. Press % to end.")
    while "%" != char:
        stack.push(char)
        char = input(" ")
    string = ""
    while stack.hasItems():
        string += stack.pop()
    print(string)

if __name__ == '__main__':
    main()
