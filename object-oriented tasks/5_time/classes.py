class Time:
    """
    Class Time. Contains attributes:

    :param hours: Contains number of hours.
    :param type: int

    :param minutes: Contains number of minutes.
    :param type: int

    :param seconds: Contains number of seconds.
    :param type: int
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        else:
            self.__hours = hours
        if minutes > 60 or minutes < 0:
            raise ValueError("Minutes must be in [0, 60] range")
        else:
            self.__minutes = minutes
        if seconds > 60 or seconds < 0:
            raise ValueError("Seconds must be in [0, 60] range")
        self.__seconds = seconds

    @property
    def hours(self) -> int:
        return self.__hours

    @property
    def minutes(self) -> int:
        return self.__minutes

    @property
    def seconds(self) -> int:
        return self.__seconds

    def add(self, other) -> None:
        seconds = self.seconds + other.seconds
        if seconds >= 60:
            seconds = seconds - 60
            self.__seconds = seconds
            if self.minutes == 59:
                self.__hours = self.hours + 1
                self.__minutes = 0
            else:
                self.__minutes = self.minutes + 1
        else:
            self.__seconds = seconds
        minutes = self.minutes + other.minutes
        if minutes >= 60:
            minutes = minutes - 60
            self.__hours = self.hours + 1
            self.__minutes = minutes
        else:
            self.__minutes = minutes
        self.__hours = self.hours + other.hours

    def substract(self, other) -> None:
        hours = self.hours - other.hours
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        else:
            self.__hours = hours
        minutes = self.minutes - other.minutes
        if minutes <= 0:
            if self.hours > 0:
                self.__hours = self.hours - 1
                self.__minutes = minutes + 60
            else:
                raise ValueError("Hours cannot be negative")
        else:
            self.__minutes = minutes
        seconds = self.seconds - other.seconds
        if seconds < 0:
            if self.minutes > 0:
                self.__minutes = self.minutes - 1
                self.__seconds = seconds + 60
            else:
                if self.hours == 0:
                    raise ValueError("Minutes cannot be negative")
                else:
                    self.__hours = self.hours - 1
                    self.__minutes = 59
        else:
            self.__seconds = seconds

    @property
    def get_hours(self) -> int:
        return self.__hours

    @property
    def get_minutes(self) -> int:
        return self.__minutes

    @property
    def get_seconds(self) -> int:
        return self.__seconds

    def __str__(self) -> str:
        formated_time = "{:02}:{:02}:{:02}".format(
            self.hours, self.minutes, self.seconds
        )
        return f"Sformatowany czas: {formated_time}"

    def add_hours(self, hours: int) -> None:
        time = Time(hours, 0, 0)
        self.add(time)

    def add_minutes(self, minutes: int) -> None:
        time = Time(0, minutes, 0)
        self.add(time)

    def add_seconds(self, seconds: int) -> None:
        time = Time(0, 0, seconds)
        self.add(time)

    def substract_hours(self, hours: int) -> None:
        time = Time(hours, 0, 0)
        self.substract(time)

    def substract_minutes(self, minutes: int) -> None:
        time = Time(0, minutes, 0)
        self.substract(time)

    def substract_seconds(self, seconds: int) -> None:
        time = Time(0, 0, seconds)
        self.substract(time)
