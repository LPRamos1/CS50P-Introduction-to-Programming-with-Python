import sys
from pathlib import Path


def main():
    # Filter for more than one command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = Path(sys.argv[1])
    # Filter for extension
    if file_path.suffix != (".py"):
        sys.exit("Not a python file")
    # Execution with error treatment
    try:
        print(count_lines(file_path))
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(filename):
    """
    Count the number of lines in .py file
    Ignores blank spaces and comments
    """
    count = 0
    with open(filename, "r") as file:
        for line in file:
            clean_line = line.lstrip()
            if not clean_line or clean_line.startswith("#"):
                continue
            count += 1
    return count


if __name__ == "__main__":
    main()
