def common_letters(first_word, second_word):
    first_word = first_word.casefold()
    second_word = second_word.casefold()
    common = ""
    for letter in range(len(first_word)):
        if (first_word[letter] in second_word) and (first_word[letter] not in common):
            common += first_word[letter]

    print("Common letters: " + ", ".join(common))


def main():
    common_letters("EckardR", "Berry")

if __name__ == "__main__":
    main()

