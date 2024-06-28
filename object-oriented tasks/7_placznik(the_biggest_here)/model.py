class InvalidNameError(Exception):
    pass


class InvalidSexError(Exception):
    pass


class Person:
    def __init__(self, id, name, sex, birth_date):
        # _ symbolizuje prywatną daną
        if not name:
            raise InvalidNameError("Name cannot be empty")
        if sex not in ("Male", "Female"):
            raise InvalidSexError("Sex has to be either Female or Male")
        self._id = id
        self._name = name
        self._sex = sex
        self._birth_date = birth_date
        self._sex = sex

    def __str__(self):
        return self._name

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def id(self):
        return self._id

    def birth_date(self):
        return self._birth_date
