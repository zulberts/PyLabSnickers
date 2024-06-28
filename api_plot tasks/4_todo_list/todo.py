import sys
import argparse
from todo_database import ToDoDatabase
from todo_plotter import pie_plotter, bar_plotter


def print_todos(todos):
    for todo in todos:
        print(todo)


def main(arguments):
    parser = argparse.ArgumentParser()

    parser.add_argument("--reset", action="store_true")
    parser.add_argument("file", nargs="?", default="todos.json")
    parser.add_argument("--user")
    parser.add_argument("--list-not-completed")
    parser.add_argument("--toggle-todo")
    parser.add_argument("--bar-plot", action="store_true")
    parser.add_argument("--pie-plot", action="store_true")

    args = parser.parse_args(arguments[1:])

    todos_db = ToDoDatabase(args.file)

    if args.reset:
        todos_db.load_todos_from_api()
    else:
        todos_db.load_todos_from_file()

    if args.user:
        print_todos(todos_db.get_todo_by_user_id(args.user))

    if args.list_not_completed:
        print_todos(todos_db.get_not_done_by_user_id(args.list_not_completed))

    if args.toggle_todo:
        todos_db.toggle_todo(args.toggle_todo)

    values = [todos_db.calculate_done(), todos_db.calculate_not_done()]

    if args.bar_plot:
        bar_plotter(values)

    if args.pie_plot:
        pie_plotter(values)


if __name__ == "__main__":
    main(sys.argv)
