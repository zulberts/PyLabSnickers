import json
import csv
from todo_classes import ToDoItem


class InvalidToDoItemPropsError(ValueError):
    def __init__(self, err) -> None:
        super().__init__(err)


class MalformedDataError(KeyError):
    pass


def load_todos(todos_json):
    todos = []
    try:
        for todo_data in todos_json:
            id = todo_data["id"]
            user_id = todo_data["userId"]
            title = todo_data["title"]
            completed = todo_data["completed"]
            try:
                todo = ToDoItem(id, user_id, title, completed)
                todos.append(todo)
            except ValueError as e:
                raise InvalidToDoItemPropsError(todo_data) from e
    except KeyError as e:
        raise MalformedDataError(str(e))
    return todos


def load_todos_from_json(filehandle):
    return load_todos(json.load(filehandle))


def load_todos_from_csv(filehandle):
    reader = csv.DictReader(filehandle)
    todos = []
    try:
        for row in reader:
            if None in row.values():
                raise MalformedDataError("A column cannot be missing")
            id = row["id"]
            user_id = row["userId"]
            title = row["title"]
            completed = row["completed"]
            try:
                todo = ToDoItem(id, user_id, title, completed)
                todos.append(todo)
            except ValueError as e:
                raise InvalidToDoItemPropsError(row) from e
    except csv.Error as e:
        raise MalformedDataError(str(e))
    return todos


def save_todos_json(filehandle, todos):
    todos_json = []
    for todo in todos:
        todos_json.append(
            {
                "userId": todo.user_id,
                "id": todo.id,
                "title": todo.title,
                "completed": todo.completed,
            }
        )
    json.dump(todos_json, filehandle, indent=4)


def save_todos_csv(filehandle, todos):
    writer = csv.DictWriter(
        filehandle, fieldnames=["id", "userId", "title", "completed"]
    )
    writer.writeheader()
    for todo in todos:
        writer.writerow(
            {
                "id": todo.id,
                "userId": todo.user_id,
                "title": todo.title,
                "completed": todo.completed,
            }
        )
