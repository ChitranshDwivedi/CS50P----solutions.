# asks user to input any kind of greeting
x = input("Greeting: ").strip().lower()

# prints amount of money based on the greeting they put in
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")
