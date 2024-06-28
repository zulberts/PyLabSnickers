import csv
from movie import Movie
import os


class MalformedCsvDataError(KeyError):
    def __init__(self, err) -> None:
        super().__init__(err)


class InvalidMoviePropsError(ValueError):
    def __init__(self, err) -> None:
        super().__init__(err)
        self.err = err


def get_files(path):
    filenames = os.walk(path)
    files = []
    for dir_path, dir_names, file_names in filenames:
        for file in file_names:
            if file[-4:] == ".csv":
                files.append(file)
    return files


def load_movies_from_file(filehandle):
    movies = []
    reader = csv.DictReader(filehandle)
    try:
        for row in reader:
            if None in row:
                raise MalformedCsvDataError("A field cannot be missing")
            title = row["title"]
            year = row["year"]
            genre = row["genre"]
            duration = row["duration"]
            description = row["description"]
            try:
                movie = Movie(title, year, genre, duration, description)
                movies.append(movie)
            except ValueError as e:
                raise InvalidMoviePropsError(str(e))
    except KeyError as e:
        raise MalformedCsvDataError(str(e))
    except csv.Error as e:
        raise MalformedCsvDataError(str(e))

    return movies
