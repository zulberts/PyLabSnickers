def policz_linie(plik):
    try:
        # Otwórz plik w trybie do odczytu
        with open(plik, "r") as file:
            # Wykorzystaj funkcję readlines() do odczytania
            # wszystkich linii z pliku
            linie = file.readlines()
            # Zlicz ilość linii
            ilosc_linii = len(linie)
            print(f"Ilość linii w pliku {plik}: {ilosc_linii}")
            return ilosc_linii
    except FileNotFoundError:
        print(f"Plik {plik} nie został znaleziony.")
        return None


# Przykład użycia
nazwa_pliku = "przykladowy_plik.txt"
liczba_linii = policz_linie(nazwa_pliku)

if liczba_linii is not None:
    print(f"Liczba linii w pliku {nazwa_pliku}: {liczba_linii}")


def zapisz_do_pliku(nazwa_pliku, zawartosc, tryb="w"):
    try:
        # Otwórz plik w trybie do zapisu (lub append, jeśli tryb='a')
        with open(nazwa_pliku, tryb) as file:
            # Zapisz zawartość do pliku
            file.write(zawartosc)
            print(f"Plik {nazwa_pliku} został pomyślnie zapisany.")
    except IOError as e:
        print(f"Wystąpił błąd wejścia/wyjścia: {e}")


# Przykład użycia
nazwa_pliku = "nowy_plik.txt"
nowa_zawartosc = "To jest nowa zawartość pliku.\nDodatkowa linijka."

# Zapisz do pliku w trybie nadpisywania ('w')
zapisz_do_pliku(nazwa_pliku, nowa_zawartosc)

# Zapisz do pliku w trybie dopisywania ('a')
# zapisz_do_pliku(nazwa_pliku, nowa_zawartosc, tryb='a')


def dopisz_do_pliku(imie, nazwisko, nazwa_pliku="dane.txt"):
    try:
        # Otwórz plik w trybie do dopisywania ('a')
        with open(nazwa_pliku, "a") as file:
            # Dopisz nową linię z imieniem i nazwiskiem
            file.write(f"{imie} {nazwisko}\n")
            print(f"Dodano {imie} {nazwisko} do pliku {nazwa_pliku}")
    except IOError as e:
        print(f"Wystąpił błąd wejścia/wyjścia: {e}")


# Przykład użycia
dopisz_do_pliku("Jan", "Kowalski")
dopisz_do_pliku("Anna", "Nowak")
