from movie import Movie
import pytest


def test_create_movie_std():
    movie = Movie(
        "sherlock", "2011", "crime", "120", "TV series about a famous detective"
    )
    assert movie.title == "sherlock"
    assert movie.duration == 120
    assert movie.year == "2011"
    assert movie.genre == "crime"
    assert movie.description == "TV series about a famous detective"


def test_create_movie_invalid():
    with pytest.raises(ValueError):
        Movie(
            "sherlock", "12..0", "2011", "crime", "TV series about a famous detective"
        )
