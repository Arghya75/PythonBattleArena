import re

def bigWord(text):
    """
    Returns the longest word from a string. If there is no text it will return no words found
    """
    # Converting the inputted text into a list
    words = re.findall(r'\b\w+\b', text)
    # Checking is there any words in the list or not
    if not words:
        return "No words found"
    # Finding the maximum word and returning it
    return max(words, key=len)

# checking do the function works appropriately
assert bigWord("Python is very easy") == "Python"
assert bigWord("arghya is arghya chakraborty") == "chakraborty"
assert bigWord("!!!") == "No words found"

# taking user input and printing the largest word
userInput = input("Enter your word: ")
print(bigWord(userInput))
