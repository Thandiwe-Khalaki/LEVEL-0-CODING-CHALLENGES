def common_letters(first_word, second_word):
    common = ""
    for letter in first_word:
        if letter in second_word:
            common += letter
    print("Common letters: " + ",".join(common))


common_letters("house", "computers")
