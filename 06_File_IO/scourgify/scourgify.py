import sys
from pathlib import Path
import csv


def main():
    # Validate command-line arguments count
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    # Validate file extension
    if input_file.suffix != ".csv":
        sys.exit("Not a CSV file")

    # Execution with error treatment
    try:
        first_last_name(input_file, output_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def first_last_name(input_path, output_path):
    """
    Reads a CSV with 'name,house' and writes a new CSV with 'first,last,house'.
    """
    with open(input_path, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        with open(output_path, "w", newline="", encoding="utf-8") as outfile:
            # New Header in the specified order
            fieldname = ["first", "last", "house"]
            new_data = csv.DictWriter(outfile, fieldnames=fieldname)
            new_data.writeheader()

            for row in reader:
                # Expected format is "fast name, first name".
                # Split to separate fast and first names.
                last, first = row["name"].split(", ")
                new_data.writerow({"first": first, "last": last, "house": row["house"]})


if __name__ == "__main__":
    main()
