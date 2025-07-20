def getNumber(prompt):
    """
    Returns a validated integer input from the user. Re-prompts if invalid input is entered.
    """
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input")

num = getNumber("Enter your number: ")
print(f"\nMultiplication Table of {num}")

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
