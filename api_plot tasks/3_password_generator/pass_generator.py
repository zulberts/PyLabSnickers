import argparse
import random
import string


def generate_password(
    min_length,
    max_length,
    separators,
    padding_digits,
    padding_symbols,
    padding_symbols_number,
    words_number,
):
    with open("words.txt", "r") as file:
        words = [
            word.strip()
            for word in file.readlines()
            if min_length <= len(word.strip()) <= max_length
        ]

    password_words = random.sample(words, words_number)
    password_core = random.choice(separators).join(password_words)
    digits = "".join(random.choices(string.digits, k=padding_digits))
    password_with_digits = digits + password_core + digits[::-1]
    symbols = "".join(random.choices(padding_symbols, k=padding_symbols_number))
    final_password = symbols + password_with_digits + symbols[::-1]

    return final_password


def main():
    parser = argparse.ArgumentParser(description="Generator haseł")
    parser.add_argument(
        "--possible_separators", type=str, required=True, help="Dozwolone separatory"
    )
    parser.add_argument(
        "--padding_digits",
        type=int,
        required=True,
        help="Liczba cyfr dopełniających hasło",
    )
    parser.add_argument(
        "--padding_symbols_number",
        type=int,
        required=True,
        help="Liczba symboli dopełniających hasło",
    )
    parser.add_argument(
        "--possible_padding_symbols",
        type=str,
        required=True,
        help="Dozwolone symbole dopełniające hasło",
    )
    parser.add_argument(
        "--words_number", type=int, required=True, help="Liczba słów w haśle"
    )
    parser.add_argument(
        "--minimal_word_length", type=int, required=True, help="Minimalna długość słowa"
    )
    parser.add_argument(
        "--maximal_word_length",
        type=int,
        required=True,
        help="Maksymalna długość słowa",
    )
    parser.add_argument(
        "--generated_passwords",
        type=int,
        required=True,
        help="Liczba generowanych haseł",
    )

    args = parser.parse_args()

    for _ in range(args.generated_passwords):
        password = generate_password(
            args.minimal_word_length,
            args.maximal_word_length,
            args.possible_separators,
            args.padding_digits,
            args.possible_padding_symbols,
            args.padding_symbols_number,
            args.words_number,
        )
        print(password)


if __name__ == "__main__":
    main()
