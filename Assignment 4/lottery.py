import random

def lotto():
    numbers = set()
    while 6 > len(numbers):
        numbers.add(random.randint(1, 49))
    return numbers

def checkNumbers(lottoNumbers, winningNumbers):
    matches = 0
    for number in winningNumbers:
        for guess in lottoNumbers:
            if guess == number:
                matches += 1
    if 2 == matches:
        return "Free Play"
    if 3 == matches:
        return "10"
    if 4 == matches:
        return "90.50"
    if 5 == matches:
        return "5000"
    if 6 == matches:
        return "13000000"

def main():
    winningNumbers = {9, 20, 27, 35, 37, 43}
    lottoNumbers = lotto()
    prize = checkNumbers(winningNumbers, lottoNumbers)
    print("9, 20, 27, 35, 37, 43")
    lottoString = ""
    for number in lottoNumbers:
        lottoString += f"{number}, "
    print(lottoString.removesuffix(", "))
    print(prize)


if __name__ == '__main__':
    main()

