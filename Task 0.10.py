def common_letters(first_word, second_word):
    """Takes two strings as input, and outputs the common characters/letters that they share"""
    common = ""
    for letter in first_word:
        if letter in second_word:
            common += letter 
    return "Common letters: " + ','.join(common)

print(common_letters("Haana","Haana"))