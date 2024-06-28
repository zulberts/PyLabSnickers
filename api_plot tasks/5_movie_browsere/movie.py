class Movie:
    def __init__(self, title, year, genre, duration, description) -> None:
        self._title = title
        self._duration = int(duration)
        self._year = year
        self._genre = genre
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def duration(self):
        return self._duration

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre

    @property
    def description(self):
        return self._description

    def __repr__(self) -> str:
        return f"{self._title}, {self._genre}, filmed in {self._year}"
