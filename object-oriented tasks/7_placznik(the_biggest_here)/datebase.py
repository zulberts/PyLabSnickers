from model_io import read_from_csv, write_to_csv
from model_io import read_from_json, write_to_json
from os.path import splitext


class PersonPathNotFound(FileNotFoundError):
    pass


class PersonPermissionError(PermissionError):
    pass


class PersonPathIsDirectory(IsADirectoryError):
    pass


class Datebase:
    def __init__(self) -> None:
        self.people = []

    def load_from_file(self, path):
        ext = splitext(path)[:-1]
        try:
            with open(path, "r") as file_handle:
                if ext == "json":
                    self.people = read_from_json(file_handle)
                else:
                    self.people = read_from_csv(file_handle)
        except FileNotFoundError:
            raise PersonPathNotFound("Could not open person datebase")
        except PermissionError:
            msg = "You do not have permissions to open the datebase"
            raise PersonPermissionError({msg})
        except IsADirectoryError:
            raise PersonPathIsDirectory("Can only work on files")

    def save_to_file(self, path):
        ext = splitext(path)[:-1]
        try:
            with open(path, "w") as file_handle:
                if ext == "json":
                    write_to_json(file_handle, self.people)
                else:
                    write_to_csv(file_handle, self.people)
        except FileNotFoundError:
            raise PersonPathNotFound("Could not open person datebase")
        except PermissionError:
            msg = "You do not have permissions to open the datebase"
            raise PersonPermissionError({msg})
        except IsADirectoryError:
            raise PersonPathIsDirectory("Can only work on files")
