#!/usr/bin/env/python3

from Media import *


def main():
    mediaLibrary = MediaLibrary()
    mediaLibrary.addMedia(Book("The Study of Orchestration", "Samuel Adler", 640))
    mediaLibrary.addMedia(Book("The Invisible Life of Addie Larue", "V.E. Schwab", 444))
    mediaLibrary.addMedia(Book("IT", "Stephen King", 1138))
    mediaLibrary.addMedia(AudioRecording("Soul Station", "Hank Mobley", 48))
    mediaLibrary.addMedia(AudioRecording("Music is Rotted One Note", "Squarepusher", 75))
    mediaLibrary.addMedia(AudioRecording("We Like It Here", "Snarky Puppy", 93))

    for media in mediaLibrary:
        print(media)

    # demonstrate modify
    print("Modify title of IT to Cujo.")
    mediaLibrary.modifyMedia("it")

    #demonstrate remove
    print("Demonstrate remove item. Soul Station is removed.")
    mediaLibrary.removeMedia("Soul Station")

    for media in mediaLibrary:
        print()



if __name__ == '__main__':
    main()