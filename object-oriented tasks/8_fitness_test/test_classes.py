from classes import Exercise, ExerciseSet
from datetime import timedelta
import pytest


def test_exercise_standard():
    Plank = Exercise("Plank", "Belly train", 50, timedelta(minutes=2))
    assert Plank.title == "Plank"
    assert Plank.info == "Belly train"
    assert Plank.kilocalories_per_minute == 50
    assert Plank.time_spent == timedelta(seconds=120)


def test_exercise_invalid():
    with pytest.raises(ValueError):
        Exercise("Plank", "Belly train", -20, timedelta(minutes=2))
    with pytest.raises(ValueError):
        Exercise("", "Belly train", -20, timedelta(minutes=2))
    with pytest.raises(ValueError):
        Exercise("dsad", "", -20, timedelta(minutes=2))
    with pytest.raises(ValueError):
        Exercise("", "Belly train", "sadsa", timedelta(minutes=2))


def test_str_():
    Plank = Exercise("Plank", "Belly train", 50, timedelta(minutes=2))
    assert Plank.__str__() == "Plank 50 kcal 0:02:00"


def test_EreciseSet():
    Plank = Exercise("Plank", "Belly train", 50, timedelta(minutes=2))
    Plank2 = Exercise("Plank", "Belly train", 50, timedelta(seconds=2))
    Planks = ExerciseSet("Planks")
    assert Planks.title == "Planks"


def test_Exercise_time():
    Plank = Exercise("Plank", "Belly train", 50, timedelta(minutes=2))
    assert Plank.total_calories == 100


def test_add_exercise():
    Plank2 = Exercise("Plank", "Belly train", 50, timedelta(minutes=2))
    Planks = ExerciseSet("Planks", 0, timedelta(0), [])
    Planks.add_exercise(Plank2)
    assert Planks.total_calories_burnt == 100
    assert Planks.total_time_spent == timedelta(minutes=2)
    assert Planks.exercises == [Plank2]


def test_add_exerciseset():