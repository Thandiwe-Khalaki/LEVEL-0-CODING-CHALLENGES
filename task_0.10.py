def common_letters(first_word, second_word):
    first,second = first_word.lower(),second_word.lower()
    common  = list(set(first) & set(second))
    return f"common: {common}"

print(common_letters("Eckard","Berry"))