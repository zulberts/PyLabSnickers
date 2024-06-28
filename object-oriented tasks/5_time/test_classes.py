from classes import Time
import pytest


def test_time_standard():
    polnoc = Time(0, 0, 0)
    assert polnoc.hours == 0
    assert polnoc.minutes == 0
    assert polnoc.seconds == 0


def test_time_invalid_0():
    with pytest.raises(ValueError):
        Time(-1, 0, 0)


def test_time_invalid_1():
    with pytest.raises(ValueError):
        Time(0, 66, 0)


def test_time_invalid_2():
    with pytest.raises(ValueError):
        Time(0, 0, 66)


def test_add():
    polnoc = Time(0, 1, 2)
    polnoc2 = Time(1, 0, 1)
    polnoc.add(polnoc2)
    assert polnoc.hours == 1
    assert polnoc.minutes == 1
    assert polnoc.seconds == 3


def test_add_2():
    polnoc = Time(0, 1, 59)
    polnoc2 = Time(1, 0, 1)
    polnoc.add(polnoc2)
    assert polnoc.hours == 1
    assert polnoc.minutes == 2
    assert polnoc.seconds == 0


def test_add_3():
    polnoc = Time(0, 1, 3)
    polnoc2 = Time(1, 59, 1)
    polnoc.add(polnoc2)
    assert polnoc.hours == 2
    assert polnoc.minutes == 0
    assert polnoc.seconds == 4


def test_add_4():
    polnoc = Time(0, 1, 59)
    polnoc2 = Time(2137, 0, 1)
    polnoc.add(polnoc2)
    assert polnoc.hours == 2137
    assert polnoc.minutes == 2
    assert polnoc.seconds == 0


def test_substract():
    polnoc = Time(0, 1, 59)
    polnoc2 = Time(0, 0, 1)
    polnoc.substract(polnoc2)
    assert polnoc.hours == 0
    assert polnoc.minutes == 1
    assert polnoc.seconds == 58


def test_substract_1():
    polnoc = Time(0, 1, 59)
    polnoc2 = Time(0, 0, 59)
    polnoc.substract(polnoc2)
    assert polnoc.hours == 0
    assert polnoc.minutes == 1
    assert polnoc.seconds == 0


def test_substract_2():
    polnoc = Time(0, 1, 9)
    polnoc2 = Time(0, 0, 59)
    polnoc.substract(polnoc2)
    assert polnoc.hours == 0
    assert polnoc.minutes == 0
    assert polnoc.seconds == 10


def test_substract_3():
    polnoc = Time(1, 0, 9)
    polnoc2 = Time(0, 0, 59)
    polnoc.substract(polnoc2)
    assert polnoc.hours == 0
    assert polnoc.minutes == 59
    assert polnoc.seconds == 10


def test_substract_4():
    polnoc = Time(1, 10, 9)
    polnoc2 = Time(0, 20, 9)
    polnoc.substract(polnoc2)
    assert polnoc.hours == 0
    assert polnoc.minutes == 50
    assert polnoc.seconds == 0


def test_str():
    polnoc = Time(1, 10, 9)
    assert polnoc.__str__() == "Sformatowany czas: 01:10:09"


def test_add_hours():
    polnoc = Time(1, 10, 9)
    polnoc.add_hours(1)
    assert polnoc.hours == 2
    assert polnoc.minutes == 10
    assert polnoc.seconds == 9


def test_add_minutes():
    polnoc = Time(1, 10, 9)
    polnoc.add_minutes(1)
    assert polnoc.hours == 1
    assert polnoc.minutes == 11
    assert polnoc.seconds == 9


def test_add_seconds():
    polnoc = Time(1, 10, 1)
    polnoc.add_seconds(1)
    assert polnoc.hours == 1
    assert polnoc.minutes == 10
    assert polnoc.seconds == 2


def test_substract_hours():
    polnoc = Time(2, 2, 2)
    polnoc.substract_hours(1)
    assert polnoc.hours == 1
    assert polnoc.minutes == 2
    assert polnoc.seconds == 2


def test_substract_minutes():
    polnoc = Time(2, 2, 2)
    polnoc.substract_minutes(1)
    assert polnoc.hours == 2
    assert polnoc.minutes == 1
    assert polnoc.seconds == 2


def test_substract_seconds():
    polnoc = Time(2, 2, 2)
    polnoc.substract_seconds(1)
    assert polnoc.hours == 2
    assert polnoc.minutes == 2
    assert polnoc.seconds == 1
