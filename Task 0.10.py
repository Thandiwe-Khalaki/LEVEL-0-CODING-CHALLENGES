def common_letters(first_word, second_word):
    common = ""
    for letter in first_word:
        if letter in second_word:
            common += letter 
    return "Common letters: " + ','.join(common)

print(common_letters("house", "computers"))