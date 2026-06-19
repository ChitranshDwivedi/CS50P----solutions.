def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0:2].isalpha():
       return False

    if len(s) < 2 or len(s) > 6:
        return False

    found_number = False
    for char in (s):
      if char.isdigit():
        if char == "0" and not found_number:
            return False
        found_number = True

      if found_number and char.isalpha():
        return False
      if not char.isalpha() and not char.isdigit():
        return False

    return True

main()
