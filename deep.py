# Gets the user's answer to the ultimate question
x = (input(" What is the Answer To The Great Question of Life, the Universe, and Everything ? ")).strip().lower() 

# Checks if the answer is correct in any of its three forms
if x == "42":
    print("Yes")

elif x == "forty two":
    print("Yes")

elif x == "forty-two":
    print("Yes")

else:
    print("No")
