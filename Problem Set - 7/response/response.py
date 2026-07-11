import validators # type: ignore

email = input("What's your email address? ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
