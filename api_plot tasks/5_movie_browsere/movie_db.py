from movie import Movie
from movie_io import load_movies_from_file


class MovieDb:
    def __init__(self, movies: list[Movie] = []) -> None:
        self._movies = movies

    @property
    def movies(self):
        return self._movies

    def get_movies_by_title(self, title):
        return [movie for movie in self._movies if movie.title == title]

    def load_movies(self, path):
        try:
            with open(path) as filehandle:
                for movie in load_movies_from_file(filehandle):
                    self._movies.append(movie)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass
