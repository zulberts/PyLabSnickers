from classes import Author, Article
import pytest
from datetime import datetime


def test_Author_standard():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    assert kuba.name == "Kuba"
    assert kuba.lastname == "Kurz"
    assert kuba.life == "Kuba lubi piwo"


def test_Author_error():
    with pytest.raises(ValueError):
        Author(1, "kurz", "Kuba lubi piwo")


def test_Article_short_information():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 30, 0)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    assert (
        artykul.short_information()
        == "Title: Psy, Text: Bardziej kochamy psy, Autors of this Article: Kuba Kurz, Anna Kurz, Date of publication: 2002-12-05 15:30:00."
    )


def test_set_Article_text():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 30, 0)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    artykul.set_text("heh")
    assert (
        artykul.short_information()
        == "Title: Psy, Text: heh, Autors of this Article: Kuba Kurz, Anna Kurz, Date of publication: 2002-12-05 15:30:00."
    )


def test_set_date():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 30, 0)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    date2 = datetime(2001, 12, 5, 15, 30, 0)
    artykul.set_date(date2)
    assert (
        artykul.short_information()
        == "Title: Psy, Text: Bardziej kochamy psy, Autors of this Article: Kuba Kurz, Anna Kurz, Date of publication: 2001-12-05 15:30:00."
    )


def test__lt__False():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 30, 0)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    date2 = datetime(2002, 12, 5, 15, 29, 0)
    artykul2 = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date2)
    assert artykul.__lt__(artykul2) is False


def test__lt__True():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 29, 10)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    date2 = datetime(2002, 12, 5, 15, 29, 50)
    artykul2 = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date2)
    assert artykul.__lt__(artykul2) is True


def test__str__():
    kuba = Author("kuba", "kurz", "Kuba lubi piwo")
    anna = Author("anna", "kurz", "anna lubi piwo")
    date = datetime(2002, 12, 5, 15, 29, 10)
    artykul = Article([kuba, anna], "Psy", "Bardziej kochamy psy", 4, date)
    assert artykul.__str__() == "Psy"
