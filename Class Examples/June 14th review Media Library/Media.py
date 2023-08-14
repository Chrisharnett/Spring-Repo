class Media:

    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @name.setter
    def setName(self, name):
        self.__name = name

    @author.setter
    def setAuthor(self, author):
        self.__author = author

    def __str__(self):
        return f"Title: {self.__name}\nAuthor: {self.__author}"


class Book(Media):

    def __init__(self, name, author, pages):
        Media.__init__(self, name, author)
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def setPages(self, pages):
        self.__pages = pages

    def __str__(self):
        return f"{Media.__str__(self)}.\nPages: {self.__pages}\n"


class AudioRecording(Media):
    def __init__(self, name, author, length):
        Media.__init__(self, name, author)
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def setLength(self, length):
        self.__length = length

    def __str__(self):
        return f"{Media.__str__(self)}\nLength: {self.__length}\n"


class MediaLibrary:
    def __init__(self):
        self.__list = []

    def addMedia(self, media):
        self.__list.append(media)

    def removeMedia(self, name):
        for media in self.__list:
            if name.lower() == media.name.lower():
                self.__list.remove(media)

    def __iter__(self):
        for media in self.__list:
            yield media

    def modifyMedia(self, name):
        for media in self.__list:
            if media.name.lower() == name.lower():
                print(media.__str__())
                print("1: edit Name")
                print("2: edit Author")
                if isinstance(media, Book):
                    print("3. edit pages")
                elif isinstance(media, AudioRecording):
                    print("3. edit length")
                choice = int(input("Choose:"))
                if 1 == choice:
                    name = input("Name: ")
                    media.setName(name)
                if 2 == choice:
                    author = input("Author: ")
                    media.setAuthor(author)
                if 3 == choice:
                    if isinstance(media, Book):
                        pages = input("Pages: ")
                        media.setPages(pages)
                    elif isinstance(media, AudioRecording):
                        length = input("Length: ")
                        media.setLength(length)
