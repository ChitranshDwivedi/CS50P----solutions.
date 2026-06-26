def main():
   plate = input("Plate: ")
   if is_valid(plate):
        print("Valid")
   else:
        print("Invalid")



def is_valid(s):
     s = s.upper()

     if not s[0:2].isalpha():
       return False

     if len(s) < 2 or len(s) > 6:
        return False

     found_number = False
     for char in s:
        if not char.isalpha() and not char.isdigit():
            return False
        elif char.isdigit():
            if char == "0" and not found_number:
                return False
            found_number = True
        elif found_number and char.isalpha():
            return False

     return True

if __name__ == "__main__":
    main()
