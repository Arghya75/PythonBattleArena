def reverse_string(text):
    reverse_string = ""

    for i in range(len(text)-1, -1, -1):
        reverse_string += text[i]

    return reverse_string

str = input("Enter your text: ")
print(f"The reverse string of your text is: {reverse_string(str)}")
