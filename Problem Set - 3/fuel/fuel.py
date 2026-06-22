while True:
    try:
        fraction = input("Fraction: ")
        parts = fraction.split("/")
        numerator = int(parts[0])
        denominator = int(parts[1])
        if numerator < 0 or numerator > denominator:
            raise ValueError
        percentage = round(100 * numerator / denominator)

    except ValueError:
        continue

    except ZeroDivisionError:
        continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")
    break
