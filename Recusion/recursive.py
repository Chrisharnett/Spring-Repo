
def fLoop(x):
    y = x
    while x > 1:
        x -= 1
        y *= x
    return y
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def main():
    num = 990
    print("The factorial of", num, "is", factorial(num))
    factorial(num)
    print(f"fLoop: The factorial of {num} is {fLoop(num)}.")

if __name__ == '__main__':
    main()

