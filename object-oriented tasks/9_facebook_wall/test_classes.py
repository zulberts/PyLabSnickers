from classes import User, Post


def test_user_classic():
    anna = User("Anna", ["Kuba", "Jakbub"], ["kocham psy"])
    assert anna.name == "Anna"
    assert anna.friends_list == ["Kuba", "Jakbub"]
    assert anna.wall == ["kocham psy"]
    anna.set_vissibility("Friends")
    anna.vissibility == 2


def test_Post_standard():
    anna = User("Anna", ["Kuba", "Jakbub"], ["kocham psy"])
    kotki = Post("kocham psy", anna)
    assert kotki.text == "kocham psy"
    assert kotki.author == anna


def test_wall_standard():
