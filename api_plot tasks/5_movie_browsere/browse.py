import argparse
import sys
from movie_db import MovieDb
from movie_io import get_files


def print_results(results, args):
    if args.d:
        print_distinct(results)
    else:
        for index, result in enumerate(results):
            print(f"result {index}: {result}")


def print_distinct(results):
    titles = [result.title for result in results]
    distinct = []
    for index, result in enumerate(results):
        result_occurance = titles.count(result.title)
        if result_occurance > 1:
            if result.title not in distinct:
                print(f"result {index}: {result} - found {result_occurance}x")
                distinct.append(result.title)
        else:
            print(f"result {index}: {result}")
            distinct.append(result.title)


def main(arguments):

    movie_database = MovieDb()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r", action="store_true", help="search for this title's occurances recursively"
    )
    parser.add_argument(
        "-d", action="store_true", help="inform about duplicate results"
    )
    parser.add_argument("path")
    parser.add_argument("--title")
    args = parser.parse_args(arguments[1:])

    if args.r:
        files = get_files(args.path)
        for file in files:
            movie_database.load_movies(f"{args.path}/{file}")
            found_results = movie_database.get_movies_by_title(args.title)
        print_results(found_results, args)

    else:
        movie_database.load_movies(args.path)
        found_results = movie_database.get_movies_by_title(args.title)
        print_results(found_results, args)


if __name__ == "__main__":
    main(sys.argv)
