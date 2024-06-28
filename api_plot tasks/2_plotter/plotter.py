import json
import matplotlib.pyplot as plt
import argparse
from datetime import datetime


def plot_data(file_path, timestamp_key, value_keys, start_date, end_date):
    # Odczyt danych z pliku JSON
    with open(file_path, "r") as file:
        data = json.load(file)

    # Przygotowanie danych do wykresu
    plot_data = {key: [] for key in value_keys}
    time_data = []

    for entry in data:
        timestamp = datetime.fromisoformat(entry[timestamp_key])
        if (start_date is None or timestamp >= start_date) and (
            end_date is None or timestamp <= end_date
        ):
            time_data.append(timestamp)
            for key in value_keys:
                plot_data[key].append(entry.get(key, None))

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    for key in value_keys:
        plt.plot(time_data, plot_data[key], label=key)
    plt.xlabel("Czas")
    plt.ylabel("Wartości")
    plt.title("Wykres danych")
    plt.legend()
    plt.savefig("wykres.pdf")
    plt.show()


def main():
    # Analiza argumentów linii komend
    parser = argparse.ArgumentParser(description="Wykres danych JSON.")
    parser.add_argument("file_path", type=str, help="Ścieżka do pliku JSON")
    parser.add_argument(
        "--timestamp",
        type=str,
        default="timestamp",
        help="Nazwa pola z czasem próbkowania",
    )
    parser.add_argument(
        "--value",
        type=str,
        nargs="+",
        required=True,
        help="Nazwa pola z wartością (można podać wiele)",
    )
    parser.add_argument(
        "--from",
        dest="from_date",
        type=lambda s: datetime.fromisoformat(s),
        help="Początek zakresu czasu (format ISO)",
    )
    parser.add_argument(
        "--to",
        dest="to_date",
        type=lambda s: datetime.fromisoformat(s),
        help="Koniec zakresu czasu (format ISO)",
    )

    args = parser.parse_args()

    # Wywołanie funkcji tworzącej wykres
    plot_data(args.file_path, args.timestamp, args.value, args.from_date, args.to_date)


if __name__ == "__main__":
    main()
