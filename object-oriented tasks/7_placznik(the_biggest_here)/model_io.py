from model import Person
import csv
import json


class MalformedPersonDataError(Exception):
    pass


class InvalidPersonError(Exception):
    def __init__(self, tokens):
        super().__init__("Invalid person data detected")
        self.tokens = tokens


def read_from_json(file_handle):
    people = []
    data = json.load(file_handle)
    for item in data:
        try:
            id = item["id"]
            name = item["name"]
            sex = item["sex"]
            birth_date = item["birth_date"]
            person = Person(id, name, sex, birth_date)
        except KeyError as e:
            raise MalformedPersonDataError("Missing key in file") from e
        except Exception as e:
            raise InvalidPersonError(item) from e
        people.append(person)
    return people


def write_to_json(file_handle, people):
    data = []
    for person in people:
        id = person.id()
        name = person.name()
        sex = person.sex()
        birth_date = person.birth_date()
        person_data = {"id": id, "name": name, "sex": sex, "birth_date": birth_date}
        data.append(person_data)
    json.dump(data, file_handle, indent=4)


def read_from_csv(file_handle):
    # 2. read date from file
    # 3. create People instances based on date
    # 4. store into a list and return that list
    # plik automatycznie zostanie zamkniety po dzialaniach
    # inaczej samemu trzeba byloby go zamknac
    people = []
    # jest to kaczkotypowanie swego rodzaju
    reader = csv.DictReader(file_handle)
    try:
        for row in reader:
            id = row["id"]
            name = row["name"]
            sex = row["sex"]
            birth_date = row["birth_date"]
            if None in row.values():
                raise MalformedPersonDataError("Missing column in file")
            try:
                person = Person(id, name, sex, birth_date)
            except Exception:
                raise InvalidPersonError(row)
            people.append(person)
    except csv.Error as e:
        raise MalformedPersonDataError(str(e))
    return people


def write_to_csv(file_handle, people):
    writer = csv.DictWriter(file_handle, ["id", "name", "sex", "birth_date"])
    writer.writeheader()
    for person in people:
        id = person.id()
        name = person.name()
        sex = person.sex()
        birth_date = person.birth_date()
        writer.writerow({"id": id, "name": name, "sex": sex, "birth_date": birth_date})
