def count_vowels_and_consonants(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    count_text = 0

    for char in text.lower():
        if char.isalpha():
            count_text += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return count_text, vowel_count, consonant_count

input_text = input("Enter your text: ")
characters, vowels, consonants = count_vowels_and_consonants(input_text)

print(f"Characters: {characters}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
