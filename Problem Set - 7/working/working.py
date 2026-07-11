import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if not match:
        raise ValueError

    h1, m1, period1, h2, m2, period2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    if period1 == "AM":
        if h1 == 12:
            h1 = 0
    else:
        if h1 != 12:
            h1 += 12

    if period2 == "AM":
        if h2 == 12:
            h2 = 0
    else:
        if h2 != 12:
            h2 += 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == "__main__":
    main()
