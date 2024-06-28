class InvalidParamType(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class File:
    """
    File Class. Contains attributes:

    :param directory: directory where the file is stored
    :type directory: str

    :param name: file's name
    :type name: str

    :param lines: number of lines in a file
    :type lines: int
    """

    def __init__(self, directory: str, name: str, lines: int) -> None:
        try:
            self.__directory = directory
            self.__name = name
            self.__lines = int(lines)
        except ValueError as e:
            raise InvalidParamType(str(e))

    @property
    def directory(self) -> str:
        return self.__directory

    @property
    def name(self) -> str:
        return self.__name

    @property
    def lines(self) -> str:
        return self.__lines
