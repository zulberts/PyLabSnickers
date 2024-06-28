from todo_database import ToDoItem, ToDoDatabase
from todo_database import load_todos, save_todos, load_todos_from_json
from todo_database import MalformedDataError
from io import StringIO
import pytest


def test_create_todo_std():
    todo = ToDoItem(1, 1, "take out the trash", False)
    assert todo.id == 1
    assert todo.title == "take out the trash"
    assert todo.user_id == 1
    assert todo.completed is False


def test_toggle_todo_std():
    todo = ToDoItem(1, 1, "take out the trash", False)
    assert todo.completed is False
    todo.toggle()
    assert todo.completed is True
    todo.toggle()
    assert todo.completed is False


def test_repr_todo_std():
    todo = ToDoItem(1, 1, "take out the trash", False)
    assert str(todo) == "To do: take out the trash, Id: 1, done: False"


def test_load_todos_std():
    todos_json = [{"id": 1, "userId": 1, "title": "title", "completed": True}]
    todos = load_todos(todos_json)
    assert todos[0].id == 1
    assert todos[0].user_id == 1
    assert todos[0].title == "title"
    assert todos[0].completed is True


def test_load_todos_malformed_data():
    todos_json = [{"id": 1, "userId": 1, "title": "title", "done": True}]
    with pytest.raises(MalformedDataError):
        load_todos(todos_json)


def test_load_todos_from_json_std():
    json_data = StringIO('[{"id":1,"userId":1,"title":"title","completed":false}]')
    todos = load_todos_from_json(json_data)
    assert todos[0].id == 1
    assert todos[0].user_id == 1
    assert todos[0].title == "title"
    assert todos[0].completed is False


def test_save_todos_std():
    todo = ToDoItem(1, 1, "do the laundry", False)
    todo_json = save_todos([todo])
    assert todo_json == [
        {"id": 1, "userId": 1, "title": "do the laundry", "completed": False}
    ]


def test_create_database_std():
    db = ToDoDatabase("path")
    assert db.todos == []


def test_database_load_todos_from_api_std(monkeypatch):
    db = ToDoDatabase("path")
    monkeypatch.setattr(db, "save_todos_to_file", lambda _: None)
    db.load_todos_from_api()
    assert db.todos[0].id == 1


def test_database_load_todos_from_api_mocked(monkeypatch):
    db = ToDoDatabase("path")
    monkeypatch.setattr(
        "classes.fetch_todos",
        lambda: [{"id": 1, "userId": 1, "title": "title", "completed": True}],
    )
    monkeypatch.setattr(db, "save_todos_to_file", lambda _: None)
    db.load_todos_from_api()
    assert db.todos[0].id == 1
    assert db.todos[0].user_id == 1
    assert db.todos[0].title == "title"
    assert db.todos[0].completed is True
