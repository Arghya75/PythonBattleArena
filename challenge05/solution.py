def getNumber(prompt):
    """
        Returns a validated integer input from the user. Re-prompts if invalid input is entered.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input!")

def factorial(num):
    """
        This function calculates the factorial
    """
    if(num < 0):
        raise ValueError("Factorial is not defined for negative numbers.")
    if(num == 0):
        return 1
    return num * factorial(num-1)

# Taking user input and calculating factorial
n = getNumber("Enter your number: ")
print(f"The factorial of {n} is {factorial(n)}")
