# imports random
import random

# allows user to set the level at which they want to play
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
        else:
            pass

    except ValueError:
        pass

# Stores the number which the user has to guess
number = random.randint(1, n)

# Prompts the user to guess until they get it right
while True:
    try:
        g = int(input("Guess: "))

        if g < 1 :
            pass

        elif g > number:
            print("Too large!")

        elif g < number:
            print("Too small!")

        elif g == number:
            print("Just right!")
            break

    except ValueError:
        pass
