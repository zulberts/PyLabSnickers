import argparse
import csv
import json
import os
from collections import Counter


def analyze_csv(
    file_path,
    include_columns=False,
    include_rows=False,
    include_unique=False,
    include_count=False,
):
    analysis = {}
    with open(file_path, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        if reader.fieldnames is None:
            raise ValueError(f"No columns found in file: {file_path}")

        if include_columns:
            analysis["columns"] = reader.fieldnames
        data = list(reader)  # Read data into memory
        if include_rows:
            analysis["rows"] = len(data)
        if include_unique or include_count:
            for fieldname in reader.fieldnames:
                values = [row[fieldname] for row in data]
                if include_unique:
                    analysis[f"unique_{fieldname}"] = len(set(values))
                if include_count:
                    analysis[f"count_{fieldname}"] = dict(Counter(values))
    return analysis


# Main function to parse arguments and analyze CSV files
def main():
    parser = argparse.ArgumentParser(description="Analyze CSV files.")
    parser.add_argument("files", nargs="+", help="List of CSV files to analyze.")
    parser.add_argument(
        "--columns", action="store_true", help="Include list of column names."
    )
    parser.add_argument(
        "--rows", action="store_true", help="Include number of data rows."
    )
    parser.add_argument(
        "--unique",
        action="store_true",
        help="Include number of unique values for each column.",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Include count of each value for each column.",
    )
    parser.add_argument("--out", help="Output file path for JSON data.")
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force overwrite of output file without asking.",
    )

    args = parser.parse_args()

    analysis_results = {}
    for file_path in args.files:
        analysis_results[file_path] = analyze_csv(
            file_path,
            include_columns=args.columns,
            include_rows=args.rows,
            include_unique=args.unique,
            include_count=args.count,
        )

    if args.out:
        if os.path.exists(args.out) and not args.force:
            response = input(f"File {args.out} already exists. Overwrite? (y/n): ")
            if response.lower() != "y":
                print("Exiting without saving to JSON.")
                return

        with open(args.out, "w", encoding="utf-8") as jsonfile:
            json.dump(analysis_results, jsonfile, indent=4)
        print(f"Analysis results saved to {args.out}")


if __name__ == "__main__":
    main()
