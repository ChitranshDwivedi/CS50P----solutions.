from datetime import date
import inflect
import sys


def main():
    user_input = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(user_input)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes(birth_date))


def minutes(birth_date):
    d2 = date.today()
    diff = d2 - birth_date
    total_minutes = diff.days * 24 * 60
    p = inflect.engine()
    words = p.number_to_words(total_minutes, andword="").capitalize()
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
