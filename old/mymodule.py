# Import modules
import math
import random

# Lambda function to calculate square
square = lambda x: x * x

# Normal function to calculate power
def calculate_power(base, exp):
    return math.pow(base, exp)

# Main program
while True:
    print("\n----- Math Utility Program -----")
    print("1. Square")
    print("2. Power")
    print("3. Random Number")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Square =", square(num))

    elif choice == 2:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print("Power =", calculate_power(base, exp))

    elif choice == 3:
        print("Random Number =", random.randint(1, 100))

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")