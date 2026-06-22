# Ask the user to input any word/combination of letters in UPPERCASE
x = input("Enter text: ")

#remove any whitespace from the string
x = x.strip()

#lowercases the user's input
x = x.lower()

# prints the output for user
print (f"{x}")
