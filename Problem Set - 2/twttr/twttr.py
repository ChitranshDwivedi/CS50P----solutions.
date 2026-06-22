text = input("Input: ").strip()
result = ""

for char in text:
    if char.lower() not in "aeiou":
        result += char
    else:
        pass
print (f"Output: {result}")
