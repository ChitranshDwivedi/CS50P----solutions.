from datetime import date
import inflect
from seasons import minutes


def test_same_day():
    assert minutes(date.today()) == "Zero minutes"


def test_known_date():
    birth_date = date(2000, 1, 1)
    expected = _expected_minutes(birth_date)
    assert minutes(birth_date) == expected


def test_leap_year():
    birth_date = date(2000, 2, 29)
    expected = _expected_minutes(birth_date)
    assert minutes(birth_date) == expected


def _expected_minutes(birth_date):
    diff = date.today() - birth_date
    total_minutes = diff.days * 24 * 60
    p = inflect.engine()
    words = p.number_to_words(total_minutes, andword="").capitalize()
    return f"{words} minutes"
