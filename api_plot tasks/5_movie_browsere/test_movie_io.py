from movie_io import load_movies_from_file, get_files
from movie_io import MalformedCsvDataError, InvalidMoviePropsError
from io import StringIO
import pytest


def test_load_movies_from_file_std():
    data = "title,year,genre,duration,description\none,2001,one,120,one\ntwo,two,two,240,two"
    filehandle = StringIO(data)
    movies = load_movies_from_file(filehandle)
    assert len(movies) == 2
    assert movies[0].title == "one"
    assert movies[0].year == "2001"
    assert movies[0].genre == "one"
    assert movies[0].duration == 120
    assert movies[0].description == "one"


def test_load_movies_from_file_malformed():
    data = (
        "title,year,genre,duration,descriptiom"
        + "\none,one,one,120,one\ntwo,two,two,240,two"
    )
    filehandle = StringIO(data)
    with pytest.raises(MalformedCsvDataError):
        load_movies_from_file(filehandle)


def test_load_movies_from_file_invalid_props():
    data = (
        "title,year,genre,duration,description"
        + "\none,one,one,120,one\ntwo,two,two,24..0,two"
    )
    filehandle = StringIO(data)
    with pytest.raises(InvalidMoviePropsError):
        load_movies_from_file(filehandle)


def test_get_files_std():
    assert get_files(".") == ["sample.csv", "forbidden.csv"]


# def test_get_files_nested_dir():
