# Converts :) and :( emoticons to their emoji equivalents.
def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

# Gets user input, converts emoticons, and prints the result.
def main():
    x = input("Enter text: ")
    print(convert(x))

# runs the code above.
main()
