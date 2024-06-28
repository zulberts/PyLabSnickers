from datetime import datetime


category_dict = {1: "Science", 2: "Sport", 3: "Technology", 4: "Politics", 5: "Fun"}


class Author:
    """
    Author class. Contains Attribues:

    :param name: Author's name
    :param type: string

    :param lastname: Author's last name
    :param type: string

    :param life: Author's short story of life
    :param type: string
    """

    def __init__(self, name: str, lastname: str, life: str) -> None:
        """
        Creates an instance of the Author class
        """
        if type(name) is not str:
            raise ValueError
        if type(lastname) is not str:
            raise ValueError
        if type(life) is not str:
            raise ValueError
        self.__name = str.title(name)
        self.__lastname = str.title(lastname)
        self.__life = str(life)

    @property
    def name(self):
        """
        Returns first name of the Author
        """
        return self.__name

    @property
    def lastname(self):
        """
        Returns last name of the Author
        """
        return self.__lastname

    @property
    def life(self):
        """
        Returns last name of the Author
        """
        return self.__life

    def set_name(self, name: str) -> None:
        """
        Set first name of the Author
        """
        self.__name = str.title(name)

    def set_lastname(self, lastname: str) -> None:
        """
        Set second name of the Author
        """
        self.__lastname = str.title(lastname)

    def set_life(self, life: str) -> None:
        """
        Set live of the Author
        """
        self.__life = str(life)


class Article(Author):
    """
    Article class. Contains Attributes:

    :param title: String containg title of the article
    :param type: str

    :param text: String containg text of the article
    :param type: str

    :param category: Value defined by the global dictionary
    :param type: int

    :param Author: List of class Author who created the artcle
    :param type: List[Author]

    :param date: Date of articles publication
    :param type: datetime
    """

    def __init__(
        self, author: list[Author], title: str, text: str, category: int, date: datetime
    ) -> None:
        """
        Creates an instance of the Article class
        """
        self.__author = author
        self.__title = str.title(title)
        self.__text = str(text)
        self.__category = int(category)
        self.__date = date

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def text(self):
        return self.__text

    @property
    def category(self):
        return self.__category

    @property
    def date(self):
        return self.__date

    def short_information(self):
        title = f"Title: {self.title}, "
        text = f"Text: {self.text}, "
        authors = "Autors of this Article:"
        for autor in self.author:
            authors += f" {autor.name} {autor.lastname},"
        date = f"Date of publication: {self.date}"
        return f"{title}{text}{authors} {date}."

    def set_text(self, text: str):
        self.__text = text

    def set_date(self, date: datetime):
        self.__date = date

    def __lt__(self, other):
        if self.date.year > other.date.year:
            return False
        elif self.date.year < other.date.year:
            return True
        else:
            if self.date.month > other.date.month:
                return False
            elif self.date.month < other.date.month:
                return True
            else:
                if self.date.day > other.date.day:
                    return False
                elif self.date.day < other.date.day:
                    return True
                else:
                    if self.date.hour > other.date.hour:
                        return False
                    elif self.date.hour < other.date.hour:
                        return True
                    else:
                        if self.date.minute > other.date.minute:
                            return False
                        elif self.date.minute < other.date.minute:
                            return True
                        else:
                            if self.date.second >= other.date.second:
                                return False
                            else:
                                return True

    def __str__(self) -> str:
        return f"{self.__title}"
