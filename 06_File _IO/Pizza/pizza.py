import sys
from pathlib import Path
from tabulate import tabulate
import csv


def main():
    # Validate command-line arguments count
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = Path(sys.argv[1])
    # Validate file extension
    if file_path.suffix != (".csv"):
        sys.exit("Not a CSV file")

    # Specific filter for menu names
    # Note: Remove this if you want the program to work with any .csv file
    allowed_menus = ["sicilian", "regular"]
    if file_path.stem not in allowed_menus:
        sys.exit("File does not exist")

    # Execution with error treatment
    try:
        convert_tabulate(file_path)
    except FileNotFoundError:
        sys.exit("File does not exist")


def convert_tabulate(filename):
    """
    Reads a CSV file, converts it to a list of dictionaries,
    and prints a formatted ASCII table
    """
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        menu = list(reader)
        print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
