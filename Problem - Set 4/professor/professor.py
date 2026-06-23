import random


def main():
    level = get_level()
    score = 0

    # Run 10 questions
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        print(f"{x} + {y} = ", end="")

        # Give the user 3 attempts per question
        for attempts in range(3):
            try:
                answer = int(input())
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    if attempts < 2:
                        print(f"{x} + {y} = ", end="")
            except ValueError:
                print("EEE")
                if attempts < 2:
                    print(f"{x} + {y} = {x + y}")

    else:
        # All 3 attempts used — reveal the correct answer
        print(f"{x} + {y} = {x + y}")

 # Print final score out of 10
    print(score)


def get_level():
    # Keep prompting until a valid level (1, 2, or 3) is entered
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Return a random number based on the difficulty level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


# Calls main
if __name__ == "__main__":
    main()
