#!/usr/bin/bin/env/python3

from Classes_animal import *
def main():
    zoo = Zoo()
    zoo.addAnimal(Donkey("Donkey1", 7))
    zoo.addAnimal(Goat("Goat1", 2))
    zoo.addAnimal(HoneyBadger("Honey Badger 1", 4))
    zoo.addAnimal(Donkey("Donkey2", 3))
    zoo.addAnimal(Goat("Goat2", 1))
    zoo.addAnimal(HoneyBadger("Honey Badger 2", 8))

    for animal in zoo:
        print(f"Can feed: {animal.can_feed()}, Noise: {animal.make_noise()}, string representation: {animal}")
    print(zoo)


if __name__ == '__main__':
    main()