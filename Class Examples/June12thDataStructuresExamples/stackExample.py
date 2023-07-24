
# import stack from objects.py
from objects import Stack

def main():
    stack = Stack()

    while True:
        value = input("Enter the next value, '%' to stop")
        if value == "%":
            break
        else:
            stack.push(value)

    while stack.hasItems():
        print(stack.pop())






if __name__ == "__main__":
    main()