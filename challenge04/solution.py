def getNumber(prompt):
    """
        This function returns an integer and handles invalid input.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def palindromeChecker(number):
    """
        Check whether a number is palindrome or not.
    """
    return "Palindrome" if str(number) == str(number)[::-1] else "Not Palindrome"

assert palindromeChecker(121) == "Palindrome"
assert palindromeChecker(123) == "Not Palindrome"
assert palindromeChecker(0) == "Palindrome"

# Taking user input
num = getNumber("Enter your number: ")

# Handling for numbers less than zero
if(num < 0):
    print("Negative numbers are not considered palindromes.")
else:
    print(palindromeChecker(num))
