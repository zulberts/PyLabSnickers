from dataclasses import dataclass


@dataclass
class ToDoItem:
    """
    ToDoItem class. Contains attributes:

    :param id: todo's id
    :type id: int

    :param completed: todo's status
    :type completed: bool

    """

    id: int | str
    _user_id: int | str
    _title: str
    _completed: bool

    def __post_init__(self):
        if self._completed == "True":
            self._completed = True
        if self._completed == "False":
            self._completed = False

    @property
    def completed(self) -> bool:
        return self._completed

    @property
    def title(self) -> str:
        return self._title

    @property
    def user_id(self) -> str | int:
        return self._user_id

    def toggle(self) -> None:
        """
        Toggles todo's status
        """
        self._completed = not self._completed

    def __repr__(self) -> str:
        return f"To do: {self._title}, Id: {self.id}, done: {self._completed}"
