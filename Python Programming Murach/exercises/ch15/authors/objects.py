from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        description = ""
        for author in self.__list:
            description += str(author) + ', '
        return description.rstrip(", ")

    def __iter__(self):
        for author in self.__list:
            yield author
    
@dataclass
class Book:
    title: str = ""
    authors: Authors = None

    def getDescription(self):
        return f"{self.title} by {self.authors}"

    def __str__(self):
        return f"{self.title} by {self.authors.__str__()}"


    
@dataclass
class Author:
    firstName: str = ""
    lastName: str = ""

    def __str__(self):
        return f"{self.firstName} {self.lastName}"




