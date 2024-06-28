from model_io import (
    read_from_csv,
    write_to_json,
    MalformedPersonDataError,
    InvalidPersonError,
)
from io import StringIO
import pytest


def test_read_from_csv():
    # data = """id,name,sex,birth_date
    # id1,name1,Female,1/1/2000
    # """
    data = "id,name,sex,birth_date\nid1,name1,Female,1/1/2000\n"
    file_handle = StringIO(data)
    people = read_from_csv(file_handle)
    assert len(people) == 1
    assert people[0].id() == "id1"


# def test_read_from_csv():
#     read_from_csv('people.txt')
# def test_read_frome_file_not_exists():
#     read_from_csv('nonexistant')
# def test_read_from_csv_directory():
#     read_from_csv('/')
# def test_read_and_write():
#     with open('people.txt', 'r') as people_txt:
#         people = read_from_csv('people.txt')
#     with open('people_saved.txt', 'w') as people_saved:
#         write_to_file(people_saved, people)


def test_read_missing_column_in_row():
    data = "id,name,sex,birth_date\nid1,name1Female,1/1/2000\n"
    file_handle = StringIO(data)
    with pytest.raises(MalformedPersonDataError):
        read_from_csv(file_handle)


def test_read_invalid_data():
    data = "id,name,sex,birth_date\nid1,name1,l,1/1/2000\n"
    file_handle = StringIO(data)
    with pytest.raises(InvalidPersonError):
        read_from_csv(file_handle)


def test_read_csv_write_json():
    file_path = "/home/zulbert/zadania/zad_8_płacznik/people.txt"
    with open(file_path) as fp:
        people = read_from_csv(fp)
        with open("people.json", "w") as jsonfp:
            write_to_json(jsonfp, people)
