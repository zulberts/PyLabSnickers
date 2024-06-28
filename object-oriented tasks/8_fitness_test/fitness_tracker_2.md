Zaimplementuj część logiki prostej aplikacji do śledzenia aktywności fizycznej. Trzymaj
się podanego poniżej API oraz przykładu - kod w przykładzie powinien zadziałać i wyświetlić
podany wynik.

## Założenia
* kilokalorie reprezentowane są typem `int` lub `float` i zawsze na nich operujemy, tj. nie przeliczamy ich na kalorie
* czas trwania ćwiczeń/zestawów/przerw reprezentowany jest jako obiekt `timedelta` z modułu `datetime`
* przygotuj testy do najważniejszych funkcjonalności programu

## API

### Klasa `Exercise`:

Klasa `Exercise` powinna reprezentować pojedyncze ćwiczenie.

- **Metody**
  - `__init__` (tworzenie obiektu z tytułem, informacją, liczbą palonych kilokalorii per minuta oraz czasem trwania)
  - `__str__` (reprezentacja napisowa, forma jak w przykładzie)

- **Pola (zaimplementowane jako `property`):**
  - `title` (tytuł ćwiczenia)
  - `info` (informacje dodatkowe o ćwiczeniu)
  - `kilocalories_burnt` (ilość spalonych kilokalorii)
  - `time_spent` (czas trwania ćwiczenia)


### Klasa `ExerciseSet`:

Klasa `ExerciseSet` powinna agregować dane związane z zestawem ćwiczeń, umożliwiając obliczenie łącznej ilości spalonych kilokalorii i czasu spędzonego na zestawie.

- **Metody:**
  - `__init__` (tworzy instancję z tytułem oraz opcjonalną listą ćwiczeń)
  - `add_exercise(exercise)` (dodaje ćwiczenie do zestawu)
  - `__str__` (reprezentacja napisowa, forma jak w przykładzie)

- **Pola (zaimplementowane jako `property`)**
  - `title` (tytuł zestawu ćwiczeń)
  - `exercises` (lista ćwiczeń)
  - `total_kilocalories_burnt` (ilość spalonych kilokalorii)
  - `total_time_spent` (czas trwania zestawu ćwiczeń)

### Klasa `Workout`:

Klasa `Workout` powinna reprezentować całą sesję treningową, składającą się z różnych zestawów ćwiczeń oraz przerw.

- **Metody:**
  - `add_exercise_set(exercise_set)` - dodaje zestaw ćwiczeń do treningu
  - `add_rest_phase(rest_phase)` - dodaje fazę przerwy o określonym czasie trwania (reprezentowaną jako obiekt `timedelta` z modułu `datetime`)
  - `__str__` (reprezentacja napisowa, forma jak w przykładzie)

- **Pola (zaimplementowane jako `property`):**
  - `title` (tytuł sesji)
  - `exercises` (lista zestawów ćwiczeń)
  - `rest_phases` (lista przerw pomiędzy zestawami)
  - `plan` (łączna lista zestawów ćwiczeń i przerw)
  - `total_kilocalories_burnt` (zwraca łączną ilość spalonych kilokalorii dla całego treningu)
  - `total_time_spent` (zwraca łączny czas trwania całego treningu)

## Przykładowe użycie:

```python
# Tworzenie ćwiczeń
plank = Exercise(
    title="Plank",
    info="Classic plank exercise",
    kilocalories_per_minute=100,
    time_spent=timedelta(seconds=30),
)
side_plank = Exercise(
    "Side plank",
    "Makes your sides hurt",
    120,
    timedelta(seconds=60),
)
deadlift = Exercise("Deadlift", "Lift with your legs!", 200, timedelta(seconds=45))
jumping_jacks = Exercise(
    "Jumping Jacks", "Cardio exercise", 150, timedelta(seconds=90)
)
skipping_rope = Exercise("Skipping rope", "Hoppity hop", 150, timedelta(minutes=5))

# Tworzenie zestawu ćwiczeń
plank_set = ExerciseSet("Planks")
plank_set.add_exercise(plank)
plank_set.add_exercise(side_plank)

weight_training_set = ExerciseSet("Weight training", [deadlift])

cardio_set = ExerciseSet("Cardio", exercises=[jumping_jacks, skipping_rope])

# Tworzenie przerwy
rest_phase_1 = timedelta(minutes=2)

# Tworzenie treningu
workout = Workout("My workout")
workout.add_exercise_set(plank_set)
workout.add_exercise_set(weight_training_set)
workout.add_rest_phase(rest_phase_1)
workout.add_exercise_set(cardio_set)

assert workout.plan == [plank_set, weight_training_set, rest_phase_1, cardio_set]

# Wyświetlanie wyników
print(workout)
print(f"Total kilocalories burnt: {workout.total_kilocalories_burnt}")
print(f"Total time spent: {workout.total_time_spent}")
```

### Wynik dla powyższego kodu

```
My workout
----------

Planks
        Plank 50.0 kcal 0:00:30
        Side plank 120.0 kcal 0:01:00

Weight training
        Deadlift 150.0 kcal 0:00:45

Rest: 0:02:00

Cardio
        Jumping Jacks 225.0 kcal 0:01:30
        Skipping rope 750.0 kcal 0:05:00


Total kilocalories burnt: 1295.0
Total time spent: 0:10:45
```

## Podpowiedzi

* https://docs.python.org/3/library/datetime.html#datetime.timedelta
* metoda `timedelta.total_seconds()`
