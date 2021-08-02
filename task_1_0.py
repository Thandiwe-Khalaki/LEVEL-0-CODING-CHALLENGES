def common_letters(first_word, second_word):
    first_word = first_word.casefold()
    second_word = second_word.casefold()
    common = ""
    for letter in set(first_word):
        if letter in set(second_word):
            common += letter

    print("Common letters: " + ", ".join(common))


def main():
    common_letters("EckardR", "Berry")

if __name__ == "__main__":
    main()

