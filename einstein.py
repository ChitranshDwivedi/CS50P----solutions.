# Assigns value of speed of light to a variable "S".
S = 300000000    # metres per second

# Squares the speed of light as required by the formula.
def square(n):
    return n * n


# Gets user input(m), calculates the answer, prints it.
def main():
    m = int(input( "m: ")) # kilograms
    E = (m * (square(S)))
    print (f"E = {E}") # joules

# Runs the code above.
main()
