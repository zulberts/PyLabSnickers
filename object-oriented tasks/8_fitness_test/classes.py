from datetime import timedelta


class Exercise:
    """
    Class Exercise. Contains attributes:

    :param title: Title of the exercise.
    :param type: str

    :param info: Some addidtional information about
                    an exercise
    :param type: str

    :param kilocalories_burnt: Amount of burnt kilocalories
    :param type: int | float

    :param time_spent: time to finish an exercise
    :param type: timedelta
    """

    def __init__(
        self,
        title: str,
        info: str,
        kilocalories_per_minute: int,
        time_spent: timedelta,
    ) -> None:
        if not title:
            raise ValueError("Exercise must contain title")
        else:
            self.__title = title
        if not info:
            self.__info = ""
        else:
            self.__info = info
        if type(kilocalories_per_minute) != (int):
            raise ValueError("Kilocalories must be in int")
        elif kilocalories_per_minute <= 0:
            raise ValueError("Kilocalories must be more than 0")
        else:
            self.__kilocalories_per_minute = kilocalories_per_minute
        if type(time_spent) != timedelta:
            raise ValueError("Time must be in timedelta")
        else:
            self.__time_spent = time_spent
        self.__total_calories = self.kilocalories_per_minute * time_spent.seconds / 60

    @property
    def title(self):
        return self.__title

    @property
    def info(self):
        return self.__info

    @property
    def kilocalories_per_minute(self):
        return self.__kilocalories_per_minute

    @property
    def time_spent(self):
        return self.__time_spent

    @property
    def total_calories(self):
        return self.__total_calories

    def __str__(self):
        title = f"{self.title}"
        kcal = f"{self.total_calories} kcal"
        time = f"{self.time_spent}"
        return f"{title} {kcal} {time}"


class ExerciseSet:
    """
    Class ExerciseSet. Contains attributes:

    :param title: Title of the exercise.
    :param type: str

    :param exercises: List of exercices belonging to this set
    :param type: list[Exercise]
    """

    def __init__(self, title: str) -> None:
        if not title:
            raise ValueError("Exercise must contain title")
        else:
            self.__title = title
        self.__total_calories_burnt = 0
        self.__total_time_spent = timedelta(seconds=0)
        self.__exercises = []

    @property
    def title(self):
        return self.__title

    @property
    def total_calories_burnt(self):
        return self.__total_calories_burnt

    @property
    def total_time_spent(self):
        return self.__total_time_spent

    @property
    def exercises(self):
        return self.__exercises

    def add_exercise(self, exercise: Exercise) -> None:
        self.__exercises.append(exercise)
        self.__total_calories_burnt += exercise.total_calories
        self.__total_time_spent += exercise.time_spent

    def __str__(self):
        title = f"{self.title}"
        output = f"{title} \n "
        for exercise in self.exercises:
            output += f"{exercise.__str__()} /n"
        return f"{title} {output}"


class Workout:
    """
    Class Workout. Contains attributes:

    :param title: Title of the exercise.
    :param type: str
    """

    def __init__(
        self,
        title: str,
    ) -> None:
        if not title:
            raise ValueError("Exercise must contain title")
        else:
            self.__title = title
        self.__total_calories_burnt = 0
        self.__total_time_spent = timedelta(seconds=0)
        self.__exercises_sets = []
        self.__rest_phases = timedelta(seconds=0)
        self.__plan = []

    @property
    def title(self):
        return self.__title

    @property
    def total_calories_burnt(self):
        return self.__total_calories_burnt

    @property
    def total_time_spent(self):
        return self.__total_time_spent

    @property
    def exercises_sets(self):
        return self.__exercises_sets

    @property
    def plan(self):
        return self.__plan

    @property
    def rest_phases(self):
        return self.__rest_phases

    def add_rest_phases(self, time: timedelta) -> None:
        self.__plan = time

    def add_exercise_set(self, set: ExerciseSet):
        self.plan.append(set)
        self.__total_calories_burnt += set.total_calories_burnt
        self.__total_time_spent += set.total_time_spent

    def __str__(self):
        first = f"My workout"
        second = f"----------"
        output = ""
        for sets in self.exercises_sets:
            output += sets.__str__()
            output += f"{self.plan}"
        return f"{first} {second} {output}"
