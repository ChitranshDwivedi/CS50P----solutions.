import emoji  # type: ignore

x = input("Input: ")

print("Output: " + emoji.emojize(x, language="alias"))
