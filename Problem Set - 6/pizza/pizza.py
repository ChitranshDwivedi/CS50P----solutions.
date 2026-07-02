import csv
import sys
from tabulate import tabulate


def main():
    validate_arguments()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)

            table_data = list(reader)

        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_arguments():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
