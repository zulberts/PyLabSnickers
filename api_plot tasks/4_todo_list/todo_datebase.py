from todo_services import fetch_todos
from todo_io import (
    load_todos,
    save_todos_csv,
    load_todos_from_csv,
    load_todos_from_json,
    save_todos_json,
)


class ToDoDatabase:
    def __init__(self, path: str) -> None:
        self._todos = []
        self._path = path

    @property
    def todos(self):
        return self._todos

    def get_todo_by_user_id(self, user_id):
        return [
            todo
            for todo in self._todos
            if (todo.user_id == user_id or todo.user_id == int(user_id))
        ]

    def get_not_done_by_user_id(self, user_id):
        return [
            todo
            for todo in self._todos
            if (todo.user_id == user_id or todo.user_id == int(user_id))
            and (todo.completed is False)
        ]

    def toggle_todo(self, id):
        for todo in self._todos:
            if todo.id == id or todo.id == int(id):
                todo.toggle()
                self.save_todos_to_file()
                return

    def load_todos_from_api(self):
        try:
            todos_json = fetch_todos()
            self._todos = load_todos(todos_json)
            self.save_todos_to_file()
        except Exception:
            pass

    def save_todos_to_file(self):
        try:
            with open(self._path, "w") as filehandle:
                ext = self._path.split(".")[1]
                match ext:
                    case "json":
                        save_todos_json(filehandle, self._todos)
                    case "csv":
                        save_todos_csv(filehandle, self._todos)

        except FileNotFoundError:
            pass
        except FileExistsError:
            pass
        except Exception:
            pass

    def load_todos_from_file(self):
        try:
            with open(self._path, "r") as filehandle:
                ext = self._path.split(".")[1]
                match ext:
                    case "json":
                        self._todos = load_todos_from_json(filehandle)
                    case "csv":
                        self._todos = load_todos_from_csv(filehandle)
        except FileNotFoundError as e:
            print(str(e))

    def calculate_done(self):
        return len([todo for todo in self._todos if todo.completed is True])

    def calculate_not_done(self):
        return len([todo for todo in self._todos if todo.completed is False])
