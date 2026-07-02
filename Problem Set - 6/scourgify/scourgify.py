import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

students = []

try:
    with open(sys.argv[1], "r") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for student in students:
            writer.writerow(student)


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
