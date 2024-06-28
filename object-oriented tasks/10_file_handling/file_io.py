import csv
import json
from file import File


class MalformedFileDataError(Exception):
    pass


class InvalidFileProperty(Exception):
    def __init__(self, args) -> None:
        super().__init__("Invalid property detected")
        self.__args = args


def load_data_from_csv(filehandle):
    reader = csv.DictReader(filehandle)
    files = []
    try:
        for row in reader:
            if None in row.values():
                raise MalformedFileDataError("Data from a column is missing")
            directory = row["directory"]
            name = row["name"]
            lines = row["lines"]
            try:
                file = File(directory, name, lines)
            except Exception:
                raise InvalidFileProperty(row)
            files.append(file)
    except csv.Error as e:
        raise MalformedFileDataError(str(e))
    return files


def load_data_from_json(filehandle):
    files = []
    data = json.load(filehandle)
    for item in data:
        try:
            directory = item["directory"]
            name = item["name"]
            lines = item["lines"]
            try:
                file = File(directory, name, lines)
            except Exception as e:
                raise InvalidFileProperty(item) from e
            files.append(file)
        except KeyError as e:
            raise MalformedFileDataError("Missing key") from e
    return files


def save_data_to_csv(filehandle, data):
    writer = csv.DictWriter(filehandle, fieldnames=["directory", "name", "lines"])
    writer.writeheader()
    for item in data:
        directory = item.directory
        name = item.name
        lines = item.lines
        writer.writerow({"directory": directory, "name": name, "lines": lines})


def save_data_to_json(filehandle, data):
    data_converted = []
    for item in data:
        directory = item.directory
        name = item.name
        lines = item.lines
        data_converted.append(
            {"directory": directory, "name": name, "lines": str(lines)}
        )
    json.dump(data_converted, filehandle, indent=4)
