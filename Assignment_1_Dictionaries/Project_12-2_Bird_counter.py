#!/usr/bin/env/python3

import pickle

FILENAME = "birds.bin"

def readFile():
    birdsSighted = {}
    try:
        with open(FILENAME, "rb") as file:
            birdsSighted = pickle.load(file)
    except FileNotFoundError:
        print(f"File not found. New file called {FILENAME} will be created when data entered.")
    return birdsSighted


def writeFile(birdsSighted):
    with open(FILENAME, "wb") as file:
        pickle.dump(birdsSighted, file)

def displayCount(birdsSighted):
    birds = list(birdsSighted.keys())
    birds.sort()
    print()
    print(f"{'Name':{'26'}}{'Count':{'5'}}")
    print("========================= =====")
    for bird in birds:
        print(f"{bird.title():{'26'}}{birdsSighted[bird]:{'<5'}}")

def addSighting(bird, birdsSighted):
    if bird in birdsSighted.keys():
        birdsSighted[bird] = birdsSighted[bird] + 1
    else:
        birdsSighted[bird] = 1
    writeFile(birdsSighted)


def main():
    print("Bird Counter Program")
    print()
    print("Enter \'x\' to exit")
    print()
    birdsSighted = readFile()
    while True:
        bird = input("Enter name of bird: ").lower()
        if bird == 'x':
            break
        else:
            addSighting(bird, birdsSighted)
    displayCount(birdsSighted)


if __name__ == '__main__':
    main()