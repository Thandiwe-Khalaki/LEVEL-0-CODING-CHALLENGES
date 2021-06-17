def string_to_vowel(word):
    """Takes in a string and then prints out all the vowels in the string"""
    vowels = []
    for letter in word.lower():
        if letter in ("aeiou"):
            if(letter not in vowels):
                vowels.append(letter)

    print("Vowels: " + ', '.join(vowels))

string_to_vowel('Thandiwe Khalaki')