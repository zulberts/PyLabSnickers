from movie import Movie
from movie_db import MovieDb
import pytest


def test_create_db_std():
    movie = Movie("a", "b", "c", 123, "d")
    movie_db = MovieDb([movie])
    assert movie_db.movies == [movie]


def test_load_db_std():
    movie_db = MovieDb()
    movie_db.load_movies("sample.csv")
    assert len(movie_db.movies) == 3
    assert movie_db.movies[0].title == "The Phantom of the Opera"
    assert movie_db.movies[0].year == "1925"


def test_load_db_file_not_found():
    movie_db = MovieDb()
    with pytest.raises(FileNotFoundError):
        movie_db.load_movies("not_found.csv")


def test_load_db_file_forbidden():
    movie_db = MovieDb()
    with pytest.raises(PermissionError):
        movie_db.load_movies("forbidden.csv")


def test_get_movies_by_title_std():
    movie1 = Movie("title_a", "b", "c", 123, "d")
    movie2 = Movie("title_b", "b", "c", 123, "d")
    movie3 = Movie("title_a", "e", "f", 321, "g")
    movie_db = MovieDb([movie1, movie2, movie3])
    assert movie_db.get_movies_by_title("title_b") == [movie2]
    assert movie_db.get_movies_by_title("title_a") == [movie1, movie3]
    assert movie_db.get_movies_by_title("title_c") == []
