from file_io import (
    load_data_from_csv,
    load_data_from_json,
    save_data_to_csv,
    save_data_to_json,
)
from file_io import MalformedFileDataError, InvalidFileProperty
from file import File
from io import StringIO
import pytest


def test_load_data_from_csv_std():
    data = "directory,name,lines\nmydir,file1,1"
    filehandle = StringIO(data)
    files = load_data_from_csv(filehandle)
    assert len(files) == 1
    assert files[0].name == "file1"
    assert files[0].directory == "mydir"
    assert files[0].lines == 1


def test_load_data_from_csv_missing_column():
    data = "directory,name,lines\nmydirfile1,1"
    filehandle = StringIO(data)
    with pytest.raises(MalformedFileDataError):
        load_data_from_csv(filehandle)


def test_load_data_from_csv_invalid_entry():
    data = "directory,name,lines\nmydir,file1,num"
    filehandle = StringIO(data)
    with pytest.raises(InvalidFileProperty):
        load_data_from_csv(filehandle)


def test_load_data_from_json_std():
    data = '[{"directory":"mydir", "name": "name1", "lines": "1"}]'
    filehandle = StringIO(data)
    files = load_data_from_json(filehandle)
    assert len(files) == 1
    assert files[0].directory == "mydir"
    assert files[0].name == "name1"
    assert files[0].lines == 1


def test_load_data_from_json_missing_key():
    data = '[{"directory":"mydir", "name": "name1"}]'
    filehandle = StringIO(data)
    with pytest.raises(MalformedFileDataError):
        load_data_from_json(filehandle)


def test_load_data_from_json_invalid_entry():
    data = '[{"directory":"mydir", "name": "name1", "lines":"num"}]'
    filehandle = StringIO(data)
    with pytest.raises(InvalidFileProperty):
        load_data_from_json(filehandle)


def test_save_data_to_csv_std():
    data = [File("mydir", "name1", "1")]
    with open("files.csv", "w") as filehandle:
        save_data_to_csv(filehandle, data)


def test_load_from_json_save_to_csv():
    data_json = '[{"directory":"mydir", "name": "name1", "lines": "1"}]'
    filehandle_json = StringIO(data_json)
    data = load_data_from_json(filehandle_json)
    with open("files.csv", "w") as filehandle_csv:
        save_data_to_csv(filehandle_csv, data)


def test_save_data_to_json_std():
    data = [File("mydir", "name1", "1")]
    with open("test_files.json", "w") as filehandle:
        save_data_to_json(filehandle, data)


def test_load_from_csv_save_to_json():
    data_csv = "directory,name,lines\nmydir,name1,1\nmydir,name2,2"
    filehandle_csv = StringIO(data_csv)
    files = load_data_from_csv(filehandle_csv)
    with open("test_files.json", "w") as filehandle_json:
        save_data_to_json(filehandle_json, files)
