import requests

urls = {"todos": "https://jsonplaceholder.typicode.com"}

methods = {"GET": "/todos"}


def fetch_todos():
    todos_json = requests.get(f"{urls['todos']}{methods['GET']}")
    return todos_json.json()
