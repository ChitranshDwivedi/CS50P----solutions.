import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count = 0

try:
    with open(sys.argv[1], "r") as file:

        for line in file:
            stripped_line = line.strip()

            if stripped_line == "":
                continue

            elif stripped_line.startswith("#"):
                continue

            else:
                count += 1

        print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
