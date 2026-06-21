names = []

while True:
    try:
        x = input("Input: ").strip().title()
        names.append(x)
    except EOFError:
        print()
        break

if len(names) == 1:
    result = names[0]
elif len(names) == 2:
    result = names[0] + " and " + names[1]
else:
    result = ", ".join(names[:-1]) + ", and " + names[-1]

print(f"Adieu, adieu, to {result}")
