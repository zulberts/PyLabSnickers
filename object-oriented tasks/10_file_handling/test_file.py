from file import File
from file import InvalidParamType
import pytest


def test_create_file_std():
    file = File("mydir", "file1", 123)
    assert file.directory == "mydir"
    assert file.name == "file1"
    assert file.lines == 123


def test_create_file_invalid_entry():
    with pytest.raises(InvalidParamType):
        File("mydir", "file1", "num")
