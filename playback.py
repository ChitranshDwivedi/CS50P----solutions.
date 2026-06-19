# Asks the user to input any combination of words.
x = input("Enter text: ")

# Strips any whitespace from the string.
x = x.strip()

# Replaces the " " between words with "..." so as to show a longer pause between each word.
x = x.replace(" " , "...")

# Prints the output for user.
print (f"{x}")
