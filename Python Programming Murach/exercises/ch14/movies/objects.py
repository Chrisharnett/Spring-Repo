from dataclasses import dataclass

@dataclass
class Movie:
    __title: str = ""
    __year: int = 0

    @property
    def title(self):
        return self.__title

    def getStr(self):
        return f"{self.__title} ({self.__year})"
